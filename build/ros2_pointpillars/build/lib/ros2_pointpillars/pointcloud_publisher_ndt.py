import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point, Quaternion, Vector3, PoseStamped
from visualization_msgs.msg import Marker, MarkerArray

from transforms3d.euler import euler2quat

import numpy as np

import pycuda.driver as cuda
import math, time

from ros2_pointpillars.util.dbscan import BoudingBoxDBSCAN
from ros2_pointpillars.util.pcd_process import point_range_filter, pointcloud2_to_array
from ros2_pointpillars.model.model_trt import PointPillars

cuda.init()
device = cuda.Device(0)
cuda_driver_context = device.make_context()

class PointCloudProcessor(Node):
    def __init__(self):
        super().__init__('pointcloud_processor')
        

        ##################################Parameter####################################################################
        self.declare_parameters(
            namespace='',
            parameters=[
                ('trt_engine', '/home/rain/PointPillars/pretrained/model_class2.trt'),
                ('pointcloud_topic', '/filtered_pointcloud'),
                ('pcd_limit_range', [-69.12, -69.12, -3.0, 69.12, 69.12, 5.0]),
                ('voxel_size' , [0.32,0.32, 8.0]),
                ('max_num_points', 16),
                ('max_num_pillars', 40000),
                ('bbox_queue_len', 200),
                ('bbox_iou_threshold', 0.01),
                ('marker_queue_size', 1000),
                ('dbscan_eps', 0.5),
                ('dbscan_min_samples', 3),
            ]
        )
        self.engine_path = self.get_parameter('trt_engine').get_parameter_value().string_value
        self.pointcloud_topic_name = self.get_parameter('pointcloud_topic').get_parameter_value().string_value
        self.pcd_limit_range_value = list(self.get_parameter('pcd_limit_range').get_parameter_value().double_array_value)
        self.voxel_size_value = list(self.get_parameter('voxel_size').get_parameter_value().double_array_value)
        self.max_num_points = self.get_parameter('max_num_points').get_parameter_value().integer_value
        self.max_num_pillars = self.get_parameter('max_num_pillars').get_parameter_value().integer_value
        self.bbox_queue_len = self.get_parameter('bbox_queue_len').get_parameter_value().integer_value
        self.bbox_iou_threshold = self.get_parameter('bbox_iou_threshold').get_parameter_value().double_value
        self.marker_queue_size = self.get_parameter('marker_queue_size').get_parameter_value().integer_value
        self.dbscan_eps = self.get_parameter('dbscan_eps').get_parameter_value().double_value
        self.dbscan_min_samples = self.get_parameter('dbscan_min_samples').get_parameter_value().integer_value


        self.CLASSES = {
            'boat': 0,
            'frontline' : 1,
        }

        #################################################################################################################

        self.subscription = self.create_subscription(
            PointCloud2,
            self.pointcloud_topic_name,
            self.pointcloud_callback,
            10)
        self.pose_subscription = self.create_subscription(
            PoseStamped,
            '/current_pose',
            self.pose_callback,
            10)
        self.bbox_publisher = self.create_publisher(MarkerArray, '/bounding_boxes', 10)
        self.publish_timer = self.create_timer(0.1, self.publish_markers)  # 주기적으로 마커를 퍼블리시하는 타이머 추가
        
        self.current_pose = None
        self.last_points = None

        #############################################Model Initialize###############################################

        self.model = PointPillars(nclasses=len(self.CLASSES), voxel_size=self.voxel_size_value, point_cloud_range=self.pcd_limit_range_value, max_num_points=self.max_num_points, max_num_pillars=self.max_num_pillars,engine_path=self.engine_path)
        
        ############################################################################################################
        
        self.class_names = list(self.CLASSES.keys())

        self.dbscan = BoudingBoxDBSCAN(eps=self.dbscan_eps, min_samples=self.dbscan_min_samples, queue_size=self.marker_queue_size)
       
        self.last_clustered_bboxes = []  


    def pointcloud_callback(self, msg):
        self.last_points = point_range_filter(pointcloud2_to_array(msg), point_range=self.pcd_limit_range_value)
       
    def pose_callback(self, msg):
        self.current_pose = msg.pose
        self.process_pointcloud(self.last_points)


    def process_pointcloud(self, points):
        if self.last_points is None:
            return
        
        #current_time = time.time()

        cuda_driver_context.push()
        lidar_bboxes, labels, scores = self.model.inference(points)
        cuda_driver_context.pop()

        #self.get_logger().info(f'{time.time() - current_time}')

        if lidar_bboxes is not None and labels is not None and scores is not None:
            clustered_bboxes = self.dbscan.clustering((lidar_bboxes, labels, scores), current_pose=self.current_pose)
            if clustered_bboxes:
                self.last_clustered_bboxes = clustered_bboxes

        



    def publish_markers(self):
        if not self.last_clustered_bboxes:
            return

        new_markers = self.create_bbox_markers(self.last_clustered_bboxes)
        marker_array = MarkerArray()
        marker_array.markers = new_markers
        self.bbox_publisher.publish(marker_array)

    def create_bbox_markers(self, clustered_bboxes):
        marker_array = []
        current_time = self.get_clock().now()
        for i, (bbox, label, score) in enumerate(clustered_bboxes):
            box_marker = self.create_box_marker(i*3, *bbox, label, current_time)
            text_marker = self.create_text_marker(i*3+1, bbox[0], bbox[1], bbox[2] + bbox[3], label, score, current_time)
            arrow_marker = self.create_arrow_marker(i*3+2, *bbox, label, current_time)
            marker_array.extend([box_marker, text_marker, arrow_marker])
        return marker_array

    def create_box_marker(self, marker_id, x, y, z, l, w, h, yaw, label, current_time):
        marker = Marker()
        marker.header.frame_id = "ndt_map"
        marker.header.stamp = current_time.to_msg()
        marker.ns = "bounding_boxes"
        marker.id = marker_id
        marker.type = Marker.CUBE
        marker.action = Marker.ADD

        marker.pose.position = Point(x=float(x), y=float(y), z=float(z))
        q = euler2quat(0, 0, float(yaw))
        marker.pose.orientation = Quaternion(x=float(q[1]), y=float(q[2]), z=float(q[3]), w=float(q[0]))

        marker.scale = Vector3(x=float(l), y=float(w), z=float(h))
        marker.color = self.get_color_for_label(label)
        
        return marker

    def create_arrow_marker(self, marker_id, x, y, z, l, w, h, yaw, label, current_time):
        marker = Marker()
        marker.header.frame_id = "ndt_map"
        marker.header.stamp = current_time.to_msg()
        marker.ns = "direction_arrows"
        marker.id = marker_id
        marker.type = Marker.ARROW
        marker.action = Marker.ADD

        marker.pose.position = Point(x=float(x), y=float(y), z=float(z))
        q = euler2quat(0, 0, float(yaw + math.pi/2))
        marker.pose.orientation = Quaternion(x=float(q[1]), y=float(q[2]), z=float(q[3]), w=float(q[0]))

        marker.scale = Vector3(x=float(l), y=float(w*0.1), z=float(h*0.1))  # Arrow size
        marker.color = ColorRGBA(r=1.0, g=1.0, b=0.0, a=0.8)  # Yellow arrow
       
        return marker

    def create_text_marker(self, marker_id, x, y, z, label, score, current_time):
        marker = Marker()
        marker.header.frame_id = "ndt_map"
        marker.header.stamp = current_time.to_msg()
        marker.ns = "object_labels"
        marker.id = marker_id
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD

        marker.pose.position = Point(x=float(x), y=float(y), z=float(z))
        marker.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

        marker.scale.z = 0.5
        marker.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
        marker.text = f"{self.class_names[int(label)]}: {score:.2f}"

        return marker

    def get_color_for_label(self, label):
        colors = [
            ColorRGBA(r=1.0, g=0.0, b=0.0, a=0.3),  # boat: Red
            ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.3),  # frontline: Green
            ColorRGBA(r=0.0, g=0.0, b=1.0, a=0.3),  # None: Blue
        ]
        return colors[int(label)]

def main(args=None):
    rclpy.init(args=args)
    pointcloud_processor = PointCloudProcessor()
    
    try:
        rclpy.spin(pointcloud_processor)
    except KeyboardInterrupt:
        pass
    finally:
        pointcloud_processor.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()