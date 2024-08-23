import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point, Quaternion, Vector3, PoseStamped, TransformStamped
from visualization_msgs.msg import Marker, MarkerArray

from transforms3d.euler import euler2quat, quat2euler
from transforms3d.quaternions import qmult


import numpy as np

import pycuda.driver as cuda
import math, time
import tf2_ros

from ros2_pointpillars.util.dbscan import BoundingBoxDBSCAN
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
                ('trt_engine', '/home/rain/PointPillars/pretrained/model_0816.trt'),
                ('pointcloud_topic', '/filtered_pointcloud'),
                ('pcd_limit_range', [-69.12, -69.12, -3.0, 69.12, 69.12, 5.0]),
                ('voxel_size' , [0.32,0.32, 8.0]),
                ('max_num_points', 16),
                ('max_num_pillars', 10000),
                ('marker_queue_size', 1000),
                ('dbscan_eps', 1.0),
                ('dbscan_min_samples', 3),
                ('dbscan_tracking_queue_distance', 2.0),
                ('dbscan_update_tracking_queue_weight', 0.1),
            ]
        )
        self.engine_path = self.get_parameter('trt_engine').get_parameter_value().string_value
        self.pointcloud_topic_name = self.get_parameter('pointcloud_topic').get_parameter_value().string_value
        self.pcd_limit_range_value = list(self.get_parameter('pcd_limit_range').get_parameter_value().double_array_value)
        self.voxel_size_value = list(self.get_parameter('voxel_size').get_parameter_value().double_array_value)
        self.max_num_points = self.get_parameter('max_num_points').get_parameter_value().integer_value
        self.max_num_pillars = self.get_parameter('max_num_pillars').get_parameter_value().integer_value
        self.marker_queue_size = self.get_parameter('marker_queue_size').get_parameter_value().integer_value
        self.dbscan_eps = self.get_parameter('dbscan_eps').get_parameter_value().double_value
        self.dbscan_min_samples = self.get_parameter('dbscan_min_samples').get_parameter_value().integer_value
        self.dbscan_tracking_queue_distance = self.get_parameter('dbscan_tracking_queue_distance').get_parameter_value().double_value
        self.dbscan_update_tracking_queue_weight = self.get_parameter('dbscan_update_tracking_queue_weight').get_parameter_value().double_value 


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
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self) 
        self.publish_timer = self.create_timer(0.1, self.publish_markers)  # 주기적으로 마커를 퍼블리시하는 타이머 추가
        
        self.current_pose = None
        self.last_points = None

        #############################################Model Initialize###############################################

        self.model = PointPillars(nclasses=len(self.CLASSES), voxel_size=self.voxel_size_value, point_cloud_range=self.pcd_limit_range_value, max_num_points=self.max_num_points, max_num_pillars=self.max_num_pillars,engine_path=self.engine_path)
        
        ############################################################################################################
        
        self.class_names = list(self.CLASSES.keys())

        self.dbscan = BoundingBoxDBSCAN(eps=self.dbscan_eps, min_samples=self.dbscan_min_samples, queue_size=self.marker_queue_size, tracking_queue_size=self.marker_queue_size, distance_threshold = self.dbscan_tracking_queue_distance, update_weight=self.dbscan_update_tracking_queue_weight)
       
        self.last_clustered_bboxes = []

        self.colors = []

        self.rng = np.random.default_rng(1000) 
        rgb_values = self.rng.random((100, 3))

        for rgb in rgb_values:
            self.colors.append(ColorRGBA(r=rgb[0], g=rgb[1], b=rgb[2], a=0.5))
            #self.colors.append(ColorRGBA(r=1.0, g=0.0, b=0.0, a=0.5))



    def pointcloud_callback(self, msg):
        self.last_points = point_range_filter(pointcloud2_to_array(msg), point_range=self.pcd_limit_range_value)
       
    def pose_callback(self, msg):
        self.current_pose = msg.pose
        self.process_pointcloud(self.last_points)


    def process_pointcloud(self, points):
        if self.last_points is None:
            return
        
        current_time = time.time()

        cuda_driver_context.push()
        lidar_bboxes, labels, scores = self.model.inference(points)
        cuda_driver_context.pop()

        self.get_logger().info(f'{time.time() - current_time}')

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

        for marker in new_markers :
            if marker.id % 2 == 0:
                self.publish_marker_tf(marker)

    def create_bbox_markers(self, clustered_bboxes):
        marker_array = []
        current_time = self.get_clock().now()
        for i, (bbox, label, score, new_bbox_check, id) in enumerate(clustered_bboxes):
            box_marker = self.create_box_marker(i*2, *bbox, new_bbox_check,id ,label, current_time)
            text_marker = self.create_text_marker(i*2+1, bbox[0], bbox[1], bbox[2] + bbox[3],new_bbox_check,id ,label, score, current_time)
            # arrow_marker = self.create_arrow_marker(i*3+2, *bbox, label, current_time)
            marker_array.extend([box_marker, text_marker])
        return marker_array

    def create_box_marker(self, marker_id, x, y, z, l, w, h, yaw, new_bbox_check, id ,label, current_time):
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
        marker.color = self.get_color_for_label(new_bbox_check , id, label)
        
        return marker

    # def create_arrow_marker(self, marker_id, x, y, z, l, w, h, yaw, label, current_time):
    #     marker = Marker()
    #     marker.header.frame_id = "ndt_map"
    #     marker.header.stamp = current_time.to_msg()
    #     marker.ns = "direction_arrows"
    #     marker.id = marker_id
    #     marker.type = Marker.ARROW
    #     marker.action = Marker.ADD

    #     marker.pose.position = Point(x=float(x), y=float(y), z=float(z))
    #     q = euler2quat(0, 0, float(yaw + math.pi/2))
    #     marker.pose.orientation = Quaternion(x=float(q[1]), y=float(q[2]), z=float(q[3]), w=float(q[0]))

    #     marker.scale = Vector3(x=float(l), y=float(w*0.1), z=float(h*0.1))  # Arrow size
    #     marker.color = ColorRGBA(r=1.0, g=1.0, b=0.0, a=0.8)  # Yellow arrow
       
    #     return marker

    def create_text_marker(self, marker_id, x, y, z, new_bbox_check ,id ,label, score, current_time):
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

        bbox_state = None
        if new_bbox_check == 0 :
            bbox_state = "Fix > "
        else :
            bbox_state = "Updating > "

        marker.text = f"{bbox_state}{self.class_names[int(label)]}{id}: {score:.2f}"
        # marker.text = f"{self.class_names[int(label)]}: {score:.2f}"
        return marker

    def get_color_for_label(self, new_bbox_check , id, label):
        # colors = [
        #     ColorRGBA(r=1.0, g=0.0, b=0.0, a=0.3),  # Pedestrian: Red
        #     ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.3),  # Cyclist: Green
        #     # ColorRGBA(r=0.0, g=0.0, b=1.0, a=0.3),  # Car: Blue
        # ]
        # return colors[int(label)]
        if new_bbox_check == 0:
            self.colors[id].a = 0.7
        else :
            self.colors[id].a = 0.4
        return self.colors[id]

    def add_rotation_to_tf(self, original_rotation, rotation_to_add):
        # ROS Quaternion을 리스트로 변환
        original_quat = [original_rotation.w, original_rotation.x, original_rotation.y, original_rotation.z]
        add_quat = [rotation_to_add.w, rotation_to_add.x, rotation_to_add.y, rotation_to_add.z]

        # 쿼터니언 곱셈 (회전 추가)
        new_quat = qmult(original_quat, add_quat)

        # 결과를 ROS Quaternion 메시지로 변환
        return Quaternion(x=new_quat[1], y=new_quat[2], z=new_quat[3], w=new_quat[0])
    
    def publish_marker_tf(self, marker):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = marker.header.frame_id  # 부모 프레임 (예: 'ndt_map')
        transform.child_frame_id = f"marker_{marker.id}_frame"  # 자식 프레임 ID

        # 마커의 위치 및 방향을 TF로 설정
        transform.transform.translation.x = marker.pose.position.x
        transform.transform.translation.y = marker.pose.position.y
        transform.transform.translation.z = marker.pose.position.z

        rotation_to_add = Quaternion()
        rotation_to_add.w, rotation_to_add.x, rotation_to_add.y, rotation_to_add.z = euler2quat(0, 0, np.pi/2)

        transform.transform.rotation = self.add_rotation_to_tf(marker.pose.orientation, rotation_to_add)

        # TF 메시지 publish
        self.tf_broadcaster.sendTransform(transform)

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