import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
import numpy as np
import struct
from sensor_msgs_py import point_cloud2 as pc2


class PointCloudFilter(Node):
    def __init__(self):
        super().__init__('pointcloud_filter')
        
        # 파라미터 선언
        self.declare_parameter('max_range', 2.0)
        self.declare_parameter('z_max', 0.0)
        
        # 파라미터 가져오기
        self.max_range = self.get_parameter('max_range').get_parameter_value().double_value
        self.z_max = self.get_parameter('z_max').get_parameter_value().double_value
        
        # 구독자와 발행자 설정
        self.subscription = self.create_subscription(
            PointCloud2,
            '/livox/lidar',
            self.callback,
            10)
        self.publisher = self.create_publisher(PointCloud2, '/filtered_pointcloud', 10)

    def pointcloud2_to_array(self, cloud_msg):
        pc = pc2.read_points(cloud_msg, field_names=("x", "y", "z", "intensity"), skip_nans=True)
        dtype = np.dtype([('x', np.float32), ('y', np.float32), ('z', np.float32), ('intensity', np.float32)])
        points_numpy = np.fromiter(pc, dtype=dtype)
        return np.stack([points_numpy['x'], points_numpy['y'], points_numpy['z'], points_numpy['intensity']], axis=-1)

    def callback(self, msg):
        # PointCloud2를 numpy 배열로 변환
        points = self.pointcloud2_to_array(msg)
        
        # 유클리디안 거리 계산
        distances = np.sqrt(np.sum(points[:, :3]**2, axis=1))
        
        # 필터링 조건
        mask = (distances >= self.max_range) & (points[:, 2] >= self.z_max)
        
        # 조건에 맞는 점들만 선택
        filtered_points = points[mask]
        
        # 필터링된 점들을 PointCloud2 메시지로 변환
        filtered_msg = PointCloud2()
        filtered_msg.header = msg.header
        filtered_msg.height = 1
        filtered_msg.width = filtered_points.shape[0]
        filtered_msg.fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1),
        ]
        filtered_msg.is_bigendian = False
        filtered_msg.point_step = 16
        filtered_msg.row_step = filtered_msg.point_step * filtered_msg.width
        filtered_msg.is_dense = True
        filtered_msg.data = filtered_points.tobytes()
        
        # 발행
        self.publisher.publish(filtered_msg)

def main(args=None):
    rclpy.init(args=args)
    node = PointCloudFilter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()