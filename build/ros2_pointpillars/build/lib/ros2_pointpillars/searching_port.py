import rclpy
from rclpy.node import Node
from visualization_msgs.msg import MarkerArray, Marker
from geometry_msgs.msg import PoseStamped, Point
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
import math
import numpy as np

class NearestMarkerPublisher(Node):
    def __init__(self):
        super().__init__('nearest_marker_publisher')
        
        # Subscribers
        self.create_subscription(MarkerArray, '/bounding_boxes', self.marker_callback, 10)
        self.create_subscription(PoseStamped, '/current_pose', self.pose_callback, 10)
        self.create_subscription(PointCloud2, '/map', self.pointcloud_callback, 10)
        
        # Publishers
        self.nearest_marker_pub = self.create_publisher(Marker, '/nearest_marker', 10)
        self.filtered_pointcloud_pub = self.create_publisher(PointCloud2, '/filtered_map', 10)
        self.arrow_pub = self.create_publisher(Marker, '/marker_direction', 10)
        
        self.current_pose = None
        self.markers = []
        self.nearest_marker = None

    def marker_callback(self, msg):
        self.markers = msg.markers
        self.find_nearest_marker()

    def pose_callback(self, msg):
        self.current_pose = msg.pose
        self.find_nearest_marker()

    def find_nearest_marker(self):
        if self.current_pose is None or not self.markers:
            return

        self.nearest_marker = min(self.markers, key=lambda m: self.distance(m.pose.position, self.current_pose.position))
        self.nearest_marker_pub.publish(self.nearest_marker)
        self.publish_direction_arrow()

    def distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

    def euler_from_quaternion(self, x, y, z, w):
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z

    def publish_direction_arrow(self):
        if self.nearest_marker is None:
            return

        arrow_marker = Marker()
        arrow_marker.header = self.nearest_marker.header
        arrow_marker.ns = "marker_direction"
        arrow_marker.id = 0
        arrow_marker.type = Marker.ARROW
        arrow_marker.action = Marker.ADD

        # Set the start point of the arrow
        arrow_marker.points.append(self.nearest_marker.pose.position)

        # Calculate the end point of the arrow
        orientation = self.nearest_marker.pose.orientation
        _, _, yaw = self.euler_from_quaternion(orientation.x, orientation.y, orientation.z, orientation.w)
        arrow_length = 2.0  # Adjust this value to change the length of the arrow
        end_point = Point()
        end_point.x = self.nearest_marker.pose.position.x + arrow_length * math.cos(yaw)
        end_point.y = self.nearest_marker.pose.position.y + arrow_length * math.sin(yaw)
        end_point.z = self.nearest_marker.pose.position.z
        arrow_marker.points.append(end_point)

        # Set the size of the arrow
        arrow_marker.scale.x = 0.1  # shaft diameter
        arrow_marker.scale.y = 0.2  # head diameter
        arrow_marker.scale.z = 0.2  # head length

        # Set the color of the arrow (red in this case)
        arrow_marker.color.r = 1.0
        arrow_marker.color.g = 0.0
        arrow_marker.color.b = 0.0
        arrow_marker.color.a = 1.0

        self.arrow_pub.publish(arrow_marker)

    def pointcloud_callback(self, msg):
        if self.nearest_marker is None:
            return

        orientation = self.nearest_marker.pose.orientation
        _, _, yaw = self.euler_from_quaternion(orientation.x, orientation.y, orientation.z, orientation.w)
        
        marker_direction = np.array([math.cos(yaw), math.sin(yaw), 0])
        
        filtered_points = []
        marker_position = np.array([self.nearest_marker.pose.position.x,
                                    self.nearest_marker.pose.position.y,
                                    self.nearest_marker.pose.position.z])
        
        for p in pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True):
            point_vector = np.array([p[0], p[1], p[2]]) - marker_position
            
            projection = np.dot(point_vector, marker_direction) * marker_direction
            
            perpendicular = point_vector - projection
            perpendicular_distance = np.linalg.norm(perpendicular)
            
            if perpendicular_distance <= 3.0:
                filtered_points.append(p)
        
        filtered_pc = pc2.create_cloud_xyz32(msg.header, filtered_points)
        self.filtered_pointcloud_pub.publish(filtered_pc)

def main(args=None):
    rclpy.init(args=args)
    node = NearestMarkerPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()