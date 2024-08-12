import os
import numpy as np
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
import rclpy
from rclpy.node import Node
import time

class PointCloudPublisher(Node):
    def __init__(self):
        super().__init__('point_cloud_publisher')
        self.publisher_ = self.create_publisher(PointCloud2, '/point_cloud', 10)
        self.timer_ = self.create_timer(0.1, self.publish_point_cloud)  # 10Hz
        self.count = 0
        self.declare_parameter('path','/02')
        self.point_cloud_path = '/mnt/mntpoint1/semantickitti_dataset/dataset/sequences' + self.get_parameter('path').get_parameter_value().string_value + '/velodyne/' # 실제 경로로 변경해야 합니다.
        self.max_count = len(os.listdir(self.point_cloud_path))

    def publish_point_cloud(self):

        if self.count >= self.max_count:
            print("end of binfile : ",self.count)
            return

        print("processing : ", self.count, "/",self.max_count)

        bin_file = os.path.join(self.point_cloud_path, f'{self.count:06d}.bin')
        points = np.fromfile(bin_file, dtype=np.float32).reshape(-1, 4)
        
    
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = 'map'

        fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1)
        ]

        point_cloud_msg = PointCloud2(
            header=header,
            height=1,
            width=points.shape[0],
            fields=fields,
            is_bigendian=False,
            point_step=(4 * 4),  # 4 필드 * 4 바이트(float32)
            row_step=points.shape[0] * (4 * 4),
            data=points.tobytes()
        )

        self.publisher_.publish(point_cloud_msg)

        
        

        self.count += 1
        

def main(args=None):
    rclpy.init(args=args)
    point_cloud_publisher = PointCloudPublisher()
    rclpy.spin(point_cloud_publisher)
    point_cloud_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()