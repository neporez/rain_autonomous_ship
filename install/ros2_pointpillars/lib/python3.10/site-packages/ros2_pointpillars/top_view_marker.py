import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Quaternion, Vector3

class TopViewConverter(Node):
    def __init__(self):
        super().__init__('top_view_converter')
        
        self.subscription = self.create_subscription(
            MarkerArray,
            '/bounding_boxes',
            self.marker_callback,
            10)
        
        self.publisher = self.create_publisher(MarkerArray, '/top_view_markers', 10)
        
        self.get_logger().info("Top View Converter node initialized")

    def marker_callback(self, msg):
        self.get_logger().info(f"Received {len(msg.markers)} markers")
        top_view_markers = MarkerArray()
        
        for marker in msg.markers:
            if marker.type == Marker.CUBE:
                top_view_marker = self.convert_to_top_view(marker)
                top_view_markers.markers.append(top_view_marker)
        
        self.publisher.publish(top_view_markers)
        self.get_logger().info(f"Published {len(top_view_markers.markers)} top view markers")

    def convert_to_top_view(self, marker):
        top_view_marker = Marker()
        top_view_marker.header = marker.header
        # Use the same frame as the original marker
        top_view_marker.header.frame_id = marker.header.frame_id
        top_view_marker.ns = "top_view_objects"
        top_view_marker.id = marker.id
        top_view_marker.type = Marker.CYLINDER
        top_view_marker.action = Marker.ADD

        top_view_marker.pose.position = Point(x=marker.pose.position.x, 
                                              y=marker.pose.position.y, 
                                              z=0.0)
        top_view_marker.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

        radius = max(marker.scale.x, marker.scale.y) / 2
        top_view_marker.scale = Vector3(x=radius*2, y=radius*2, z=0.1)

        top_view_marker.color = marker.color
        top_view_marker.lifetime = marker.lifetime


        return top_view_marker

def main(args=None):
    rclpy.init(args=args)
    node = TopViewConverter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()