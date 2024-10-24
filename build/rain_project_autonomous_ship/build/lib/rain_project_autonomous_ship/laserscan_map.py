import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, LaserScan
from geometry_msgs.msg import PoseStamped
import sensor_msgs_py.point_cloud2 as pc2
from transforms3d.euler import quat2euler


class LaserScanMap(Node):
    def __init__(self):
        super().__init__('laserscan_map')

        self.declare_parameters(
            namespace='',
            parameters=[
                ('slam_map_topic_name', '/map'),
                ('pose_topic_name','/current_pose'),
                ('map_angle_range',[-180, 180]),
                ('map_laser_range',[0.0, 100.0]),
                ('laserscan_angle_increment', 0.3),
                ('map_vertical_fov_range', [-15,15]),
                ('visualize_frame', 'ndt_map'),
            ]
        )

        self.slam_map_topic_name = self.get_parameter('slam_map_topic_name').get_parameter_value().string_value
        self.pose_topic_name = self.get_parameter('pose_topic_name').get_parameter_value().string_value
        self.map_angle_range = list(self.get_parameter('map_angle_range').get_parameter_value().integer_array_value)
        self.map_laser_range = list(self.get_parameter('map_laser_range').get_parameter_value().double_array_value)
        self.laserscan_angle_increment = self.get_parameter('laserscan_angle_increment').get_parameter_value().double_value
        self.map_vertical_fov_range = list(self.get_parameter('map_vertical_fov_range').get_parameter_value().integer_array_value)
        self.visualize_frame = self.get_parameter('visualize_frame').get_parameter_value().string_value


        super().__init__('laserscan_map_creator')
        self.pointcloud_sub = self.create_subscription(
            PointCloud2,
            self.slam_map_topic_name,
            self.pointcloud_callback,
            10)
        self.pose_sub = self.create_subscription(
            PoseStamped,
            self.pose_topic_name,
            self.pose_callback,
            10)
        
        self.laserscan_pub = self.create_publisher(LaserScan, '/rain/project_autonomous_ship/map_2d', 10)
    
        
        self.current_pose = None
        self.map_points = None
        
        self.min_angle = np.radians(self.map_angle_range[0])
        self.max_angle = np.radians(self.map_angle_range[1])

        self.min_range = self.map_laser_range[0]
        self.max_range = self.map_laser_range[1] 

        self.angle_increment = np.radians(self.laserscan_angle_increment)  

        self.vertical_fov_min = np.radians(self.map_vertical_fov_range[0])
        self.vertical_fov_max = np.radians(self.map_vertical_fov_range[1])

    def pointcloud_callback(self, msg):
        self.map_points = msg

    def pose_callback(self, msg):
        self.current_pose = msg.pose

        if self.current_pose is None or self.map_points is None:
            return

        points = pc2.read_points(self.map_points, field_names=("x", "y", "z"), skip_nans=True)
        transformed_points = self.transform_pointcloud(points, self.current_pose)
        scan_ranges = self.process_pointcloud(transformed_points)
        self.publish_laserscan(scan_ranges)

        

    def transform_pointcloud(self, points, pose):
        position = pose.position
        orientation = pose.orientation
       
        _, _, yaw = quat2euler([orientation.w,orientation.x, orientation.y, orientation.z])
        
        cos_yaw = np.cos(yaw)
        sin_yaw = np.sin(yaw)
        
        translation = np.array([position.x, position.y])
        transformed_points = []
        
        for point in points:
            x, y, z = point
            
            point_2d = np.array([x, y]) - translation
            
            x_new = point_2d[0] * cos_yaw + point_2d[1] * sin_yaw
            y_new = -point_2d[0] * sin_yaw + point_2d[1] * cos_yaw
            
            transformed_points.append((x_new, y_new, z))
        
        return transformed_points

    def process_pointcloud(self, points):
        num_bins = int((self.max_angle - self.min_angle) / self.angle_increment)
        scan_ranges = np.full(num_bins, np.inf)
        
        for point in points:
            x, y, z = point
            
            distance = np.sqrt(x**2 + y**2)
            angle = np.arctan2(y, x)
            elevation_angle = np.arctan2(z, distance)
            
            if self.vertical_fov_min <= elevation_angle <= self.vertical_fov_max:
                bin_index = int((angle - self.min_angle) / self.angle_increment)
                
                if 0 <= bin_index < num_bins:
                    if distance < scan_ranges[bin_index]:
                        scan_ranges[bin_index] = distance
        
        scan_ranges = np.clip(scan_ranges, self.min_range, self.max_range)
        return scan_ranges

    def publish_laserscan(self, scan_ranges):
        scan_msg = LaserScan()
        scan_msg.header.frame_id = self.visualize_frame
        scan_msg.header.stamp = self.get_clock().now().to_msg()
        scan_msg.angle_min = self.min_angle
        scan_msg.angle_max = self.max_angle
        scan_msg.angle_increment = self.angle_increment
        scan_msg.range_min = self.min_range
        scan_msg.range_max = self.max_range
        scan_msg.ranges = scan_ranges.tolist()
        
        self.laserscan_pub.publish(scan_msg)

def main(args=None):
    rclpy.init(args=args)
    
    node = LaserScanMap()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()