import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
import numpy as np
import os

class PointCloudToBinaryConverter(Node):
    def __init__(self):
        super().__init__('pointcloud_to_binary_converter')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/filtered_pointcloud',
            self.pointcloud_callback,
            10)

        self.output_dir = "/mnt/mntpoint1/Andong_dataset/0725_overlap3_bin/5/"
        self.frame_count = -1

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            self.get_logger().info(f"Created output directory: {self.output_dir}")

    def pointcloud_callback(self, msg):
        self.frame_count += 1
        
        pc = pc2.read_points(msg, field_names=("x", "y", "z", "intensity"), skip_nans=True)
        dtype = np.dtype([('x', np.float32), ('y', np.float32), ('z', np.float32), ('intensity', np.float32)])
        points_numpy = np.fromiter(pc, dtype=dtype)
        
        filename = os.path.join(self.output_dir, f"{self.frame_count:06d}.bin")
        points_numpy.tofile(filename)
        self.get_logger().info(f"Saved point cloud to {filename}")

def main(args=None):
    rclpy.init(args=args)
    
    converter = PointCloudToBinaryConverter()
    
    try:
        rclpy.spin(converter)
    except KeyboardInterrupt:
        pass
    finally:
        converter.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()