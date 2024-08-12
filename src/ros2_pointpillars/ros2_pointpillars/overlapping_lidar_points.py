import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs_py import point_cloud2
import numpy as np
from collections import deque

class PointCloudOverlapPublisher(Node):
    def __init__(self):
        super().__init__('pointcloud_overlap_publisher')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/livox/lidar',
            self.listener_callback,
            10)
        
        self.declare_parameter('overlap', 0)

        self.overlap_len = self.get_parameter('overlap').get_parameter_value().integer_value

        self.publisher = self.create_publisher(PointCloud2, 'output_pointcloud', 10)
        
        self.frame_buffer = deque(maxlen=self.overlap_len)

    def listener_callback(self, msg):
        # Convert PointCloud2 to numpy array, including intensity
        pc = point_cloud2.read_points(msg, field_names=("x", "y", "z", "intensity"), skip_nans=True)
        points = np.array(list(pc))
        
        # Add current frame to buffer
        self.frame_buffer.append(points)

        
        
        # If we have at least 3 frames, create and publish overlapped point cloud
        if len(self.frame_buffer) == self.overlap_len:
            overlapped_points = np.concatenate(list(self.frame_buffer))
            
            # Create new PointCloud2 message
            header = msg.header
            header.stamp = self.get_clock().now().to_msg()
            
            fields = [
                PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
                PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
                PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
                PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1),
            ]
            
            new_msg = point_cloud2.create_cloud(header, fields, overlapped_points)

            # Publish the new message
            self.publisher.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    node = PointCloudOverlapPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()