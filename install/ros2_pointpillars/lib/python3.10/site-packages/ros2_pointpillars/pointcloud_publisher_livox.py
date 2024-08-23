import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Point, Quaternion, Vector3
from visualization_msgs.msg import Marker, MarkerArray
from sensor_msgs_py import point_cloud2 as pc2
from transforms3d.euler import euler2quat

import numpy as np
import torch
import sys
import os
import math
import time

model_path = "/home/rain/PointPillars_train"
sys.path.append(model_path)

from utils import setup_seed, read_points, keep_bbox_from_lidar_range, vis_pc
from model import PointPillars

class PointCloudProcessor(Node):
    def __init__(self):
        super().__init__('pointcloud_processor')
        
        self.declare_parameter('ckpt', '')
        self.ckpt = self.get_parameter('ckpt').get_parameter_value().string_value

        if not self.ckpt:
            self.get_logger().error('ckpt parameter is not set!')
            return

        self.subscription = self.create_subscription(
            PointCloud2,
            '/filtered_pointcloud',
            self.pointcloud_callback,
            10)
        self.bbox_publisher = self.create_publisher(MarkerArray, 'bounding_boxes', 10)
        

        self.timer = self.create_timer(0.01, self.timer_callback)

        self.CLASSES = {
            'boat': 0,
            'frontline' : 1   
        }
        self.class_names = list(self.CLASSES.keys())

        self.pcd_limit_range = np.array([-69.12, -69.12, -3.0, 69.12, 69.12, 5.0], dtype=np.float32)
        
        self.model = PointPillars(nclasses=2, voxel_size=[0.32,0.32,8], point_cloud_range=[-69.12, -69.12, -3, 69.12, 69.12, 5], max_num_points=16).cuda()
        self.model.load_state_dict(torch.load(self.ckpt))

        # self.model_pre = PointPillarsPre(point_cloud_range=[-69.12, -69.12, -3, 69.12, 69.12, 5],voxel_size=[0.32,0.32,4]).cuda()
        # self.model = PointPillarsCore(nclasses=len(self.CLASSES),point_cloud_range=[-69.12, -69.12, -3, 69.12, 69.12, 5],voxel_size=[0.32,0.32,4]).cuda()
        # self.model.load_state_dict(torch.load(self.ckpt))
        # self.model_post = PointPillarsPos(nclasses=len(self.CLASSES)).cuda()
        
        
        self.model.eval()
        
        self.prev_markers = {}
        self.count = 0
        self.marker_lifetime = 0.2
        self.latest_points = None

    def point_range_filter(self,pts, point_range=[-69.12, -69.12, -3.0, 69.12, 69.12, 5.0]): #point_range=[0, -39.68, -3, 69.12, 39.68, 1]):
        '''
        data_dict: dict(pts, gt_bboxes_3d, gt_labels, gt_names, difficulty)
        point_range: [x1, y1, z1, x2, y2, z2]
        '''
        flag_x_low = pts[:, 0] > point_range[0]
        flag_y_low = pts[:, 1] > point_range[1]
        flag_z_low = pts[:, 2] > point_range[2]
        flag_x_high = pts[:, 0] < point_range[3]
        flag_y_high = pts[:, 1] < point_range[4]
        flag_z_high = pts[:, 2] < point_range[5]
        keep_mask = flag_x_low & flag_y_low & flag_z_low & flag_x_high & flag_y_high & flag_z_high
        pts = pts[keep_mask]
        return pts 


    def pointcloud_callback(self, msg):
        
        self.latest_points = self.point_range_filter(self.pointcloud2_to_array(msg))


    def timer_callback(self):
       
        if self.latest_points is None:
            return
        pre_time = time.time()
        pc_torch = torch.from_numpy(self.latest_points).cuda()
       

        with torch.no_grad():
            result_filter = self.model(batched_pts=[pc_torch], mode='test')[0]

         
        try :
            result_filter = keep_bbox_from_lidar_range(result_filter, self.pcd_limit_range)
        except : 
            return
        lidar_bboxes = result_filter['lidar_bboxes']
        labels, scores = result_filter['labels'], result_filter['scores']
        bbox_msg = self.create_bbox_markers(lidar_bboxes, labels, scores)
        self.bbox_publisher.publish(bbox_msg)
        print("Model inference time:", time.time() - pre_time)
        
        

    def pointcloud2_to_array(self, cloud_msg):
        pc = pc2.read_points(cloud_msg, field_names=("x", "y", "z", "intensity"), skip_nans=True)
        dtype = np.dtype([('x', np.float32), ('y', np.float32), ('z', np.float32), ('intensity', np.float32)])
        points_numpy = np.fromiter(pc, dtype=dtype)
        return np.stack([points_numpy['x'], points_numpy['y'], points_numpy['z'], points_numpy['intensity']], axis=-1)

    def array_to_pointcloud2(self, points_array):
        msg = PointCloud2()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "livox_frame"
        msg.height = 1
        msg.width = points_array.shape[0]
        msg.fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1)
        ]
        msg.is_bigendian = False
        msg.point_step = 16
        msg.row_step = msg.point_step * points_array.shape[0]
        msg.is_dense = True
        msg.data = points_array.tobytes()
        return msg

    def create_bbox_markers(self, bboxes, labels, scores):
        marker_array = MarkerArray()
        current_markers = {}

        for i, (bbox, label, score) in enumerate(zip(bboxes, labels, scores)):
            if score < 0.8 :
                continue
            box_marker = self.create_box_marker(i, *bbox, label)
            text_marker = self.create_text_marker(i, bbox[0], bbox[1], bbox[2] + bbox[3], label, score)
            
            marker_array.markers.extend([box_marker, text_marker])
            current_markers[i] = box_marker
            current_markers[f"text_{i}"] = text_marker

        for prev_id, prev_marker in self.prev_markers.items():
            if prev_id not in current_markers:
                prev_marker.action = Marker.DELETE
                marker_array.markers.append(prev_marker)

        self.prev_markers = current_markers
        return marker_array

    def create_box_marker(self, marker_id, x, y, z, l, w, h, yaw, label):
        marker = Marker()
        marker.header.frame_id = "livox_frame"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "bounding_boxes"
        marker.id = marker_id
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.pose.position = Point(x=float(x), y=float(y), z=float(z))
        q = euler2quat(0, 0, float(-yaw))
        marker.pose.orientation = Quaternion(x=float(q[1]), y=float(q[2]), z=float(q[3]), w=float(q[0]))
        marker.scale = Vector3(x=float(l), y=float(w), z=float(h))
        marker.color = self.get_color_for_label(label)
        marker.lifetime = rclpy.duration.Duration(seconds=self.marker_lifetime).to_msg()
        return marker

    def create_text_marker(self, marker_id, x, y, z, label, score):
        marker = Marker()
        marker.header.frame_id = "livox_frame"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "object_labels"
        marker.id = marker_id
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD
        marker.pose.position = Point(x=float(x), y=float(y), z=float(z))
        marker.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        marker.scale.z = 0.5
        marker.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
        marker.text = f"{self.class_names[int(label)]}: {score:.2f}"
        marker.lifetime = rclpy.duration.Duration(seconds=self.marker_lifetime).to_msg()
        return marker

    def get_color_for_label(self, label):
        colors = [
            ColorRGBA(r=1.0, g=0.0, b=0.0, a=0.3),  # Pedestrian: Red
            ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.3),  # Cyclist: Green
            # ColorRGBA(r=0.0, g=0.0, b=1.0, a=0.3),  # Car: Blue
        ]
        return colors[int(label)]

def main(args=None):
    rclpy.init(args=args)
    pointcloud_processor = PointCloudProcessor()
    rclpy.spin(pointcloud_processor)
    pointcloud_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()