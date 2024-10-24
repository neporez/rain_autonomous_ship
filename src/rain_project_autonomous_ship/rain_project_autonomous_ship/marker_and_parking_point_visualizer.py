import rclpy
import tf2_ros
import numpy as np

from rclpy.node import Node
from std_msgs.msg import ColorRGBA
from det_msgs.msg import ClusteredDetectedObjects
from geometry_msgs.msg import Point, Quaternion, Vector3, PoseStamped, TransformStamped

from visualization_msgs.msg import Marker, MarkerArray

from transforms3d.euler import euler2quat, quat2euler
from transforms3d.quaternions import qmult

from rain_project_autonomous_ship.util.parking_point_generator import ParkingPointGenerator


import math

class MarkerAndParkingPointVisualizer(Node):
    def __init__(self):
        super().__init__('marker_and_parking_point_visualizer')


        self.declare_parameters(
            namespace='',
            parameters=[
                ('port_length', 32.0),
                ('port_width', 5.6),
                ('boat_distance', 4.3),
                ('visualize_frame', 'ndt_map'),
            ]
        )

        self.port_length = self.get_parameter('port_length').get_parameter_value().double_value
        self.port_half_width = self.get_parameter('port_width').get_parameter_value().double_value/2
        self.boat_distance = self.get_parameter('boat_distance').get_parameter_value().double_value
        self.visualize_frame = self.get_parameter('visualize_frame').get_parameter_value().string_value

        self.clustered_detected_objects_subscription = self.create_subscription(ClusteredDetectedObjects, '/rain/det/clustered_detected_objects',self.clustered_detected_objects_callback,10)
        
        self.clustered_bbox_publisher = self.create_publisher(MarkerArray, '/rain/project_autonomous_ship/clustered_bounding_boxes', 10)

        self.parking_points_publisher = self.create_publisher(MarkerArray, '/rain/project_autonomous_ship/parking_points',10)
        self.goal_point_pose_publisher = self.create_publisher(PoseStamped, '/rain/project_autonomous_ship/target_point', 10)

        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        self.markers_publish_timer = self.create_timer(0.1, self.publish_markers)

        
        self.last_clustered_bboxes = []

        self.colors = []
        self.CLASSES = {
            'boat': 0,
            'frontline' : 1,
        }
        self.class_names = list(self.CLASSES.keys())

        self.rng = np.random.default_rng(1003)
        rgb_values = self.rng.random((100,3))

        for rgb in rgb_values:
            self.colors.append(ColorRGBA(r=rgb[0], g=rgb[1], b=rgb[2], a=0.5))

        self.parking_point_generator = ParkingPointGenerator()

        self.generator_parking_point_check = False

    
    
    def clustered_detected_objects_callback(self, msg: ClusteredDetectedObjects):

        lidar_bboxes = np.array(msg.bboxes).reshape(msg.bboxes_num,-1)
        labels = msg.labels
        scores = msg.scores
        new_bbox_check = msg.new_bbox_check
        id = msg.id

        self.last_clustered_bboxes = [(lidar_bboxes[i], labels[i],scores[i],new_bbox_check[i],id[i]) for i in range(msg.bboxes_num)]


    def publish_markers(self):
        if not self.last_clustered_bboxes:
            return
        
        new_markers = self.create_bbox_markers(self.last_clustered_bboxes)
        
        marker_array = MarkerArray()
        marker_array.markers = new_markers
        self.clustered_bbox_publisher.publish(marker_array)

        for marker in new_markers :
            if marker.id % 2 == 0:
                self.publish_marker_tf(marker)

        if self.generator_parking_point_check == False :
            frontline, boat = None, None
            frontline_x, frontline_y = None, None
            boat_x, boat_y, boat_dir = None, None, None
            
            for bbox, label, _, _, _ in self.last_clustered_bboxes :
                if int(label) == 0 and boat == None:
                    boat = bbox
                    boat_x, boat_y = bbox[0], bbox[1]

                if int(label) == 1 and frontline == None:
                    frontline = bbox
                    frontline_x, frontline_y = bbox[0], bbox[1]
                
                if boat is not None and frontline is not None:
                    self.generator_parking_point_check = True
                    boat_dir = self.determine_relative_position(boat, frontline)
                    self.parking_point_generator.generate_points(p1=(frontline_x, frontline_y),p2=(boat_x,boat_y),target_bar=boat_dir, bar_length=self.port_length, bar_distance=self.port_half_width, point_distance=self.boat_distance)
        else :
            
            boat_yaw_avg = float(sum(bbox[6] for bbox,_,_,_,_ in self.last_clustered_bboxes) / len(self.last_clustered_bboxes))

            parker_points, target_point = self.create_parking_points_marker_array(self.parking_point_generator.get_result(), marker_array,boat_yaw_avg)

            self.parking_points_publisher.publish(parker_points)
            self.goal_point_pose_publisher.publish(target_point)


    def create_parking_points_marker_array(self, points, boat_marker_array, boat_yaw_avg):
        marker_array = MarkerArray()
        marker = Marker()
        marker.header.frame_id = self.visualize_frame  # Adjust as needed
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "points"
        marker.id = 0
        marker.type = Marker.POINTS
        marker.action = Marker.ADD
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.5  # Point size
        marker.scale.y = 0.5
       
        boat_position_idx = []
        
        for i,(x,y) in enumerate(points):
            for boat_marker in boat_marker_array.markers :
                if  (boat_marker.id % 2 == 0) and ((((boat_marker.pose.position.x - x)**2 + (boat_marker.pose.position.y - y)**2)**(1/2)) < 2.0) :
                    boat_position_idx.append(i)

        empty_position_idx = [i for i in range(len(points)) if i not in boat_position_idx][1:]

        target_point = PoseStamped()
        target_point.header.frame_id = self.visualize_frame
        target_point.header.stamp = self.get_clock().now().to_msg()



        for i,(x, y) in enumerate(points):
            point = Point()
            point.x = float(x)
            point.y = float(y)
            point.z = 1.0  # Assuming 2D points
            marker.points.append(point)
            
            if i in boat_position_idx :
                marker.colors.append(ColorRGBA(r=1.0, g=0.0, b=0.0, a=1.0))
            elif i in empty_position_idx:
                marker.colors.append(ColorRGBA(r=0.0, g=1.0, b=0.0, a=1.0))
            else :
                marker.colors.append(ColorRGBA(r=0.0, g=0.0, b=1.0, a=1.0))
                target_point.pose.position.x = point.x
                target_point.pose.position.y = point.y
                target_point.pose.position.z = point.z

                q = euler2quat(0, 0, boat_yaw_avg + np.pi/2)

                target_point.pose.orientation = Quaternion(x=float(q[1]), y=float(q[2]), z=float(q[3]), w=float(q[0]))


    
        marker_array.markers.append(marker)
        return marker_array, target_point



    def create_bbox_markers(self, clustered_bboxes):
        marker_array = []
        current_time = self.get_clock().now()
        frontline_bbox = None
        boat_bboxes = []

        # frontline과 boat의 bbox를 분류합니다
        for bbox, label, score, new_bbox_check, id in clustered_bboxes:
            if int(label) == 1:  # frontline
                frontline_bbox = bbox
            elif int(label) == 0:  # boat
                boat_bboxes.append((bbox, score, new_bbox_check, id))

        for i, (bbox, label, score, new_bbox_check, id) in enumerate(clustered_bboxes):
            relative_position = ""
            if int(label) == 0 and frontline_bbox is not None:  # boat이고 frontline이 존재할 때
                relative_position = self.determine_relative_position(bbox, frontline_bbox)
            
            box_marker = self.create_box_marker(i*2, *bbox, new_bbox_check, id, label, current_time)
            text_marker = self.create_text_marker(i*2+1, bbox[0], bbox[1], bbox[2] + bbox[3], new_bbox_check, id, label, score, relative_position, current_time)
            marker_array.extend([box_marker, text_marker])

        return marker_array
    
    def determine_relative_position(self, boat, frontline):
        # boat의 방향 벡터 계산
        boat_direction = np.array([math.cos(boat[6]+np.pi/2), math.sin(boat[6]+np.pi/2)])
        
        # boat에서 frontline으로의 벡터
        to_frontline = np.array([frontline[0] - boat[0], frontline[1] - boat[1]])
        
        # 외적 계산
        cross_product = np.cross(boat_direction, to_frontline)
        
        if cross_product > 0:
            return "left"
        else:
            return "right"

    def create_box_marker(self, marker_id, x, y, z, l, w, h, yaw, new_bbox_check, id ,label, current_time):
        marker = Marker()
        marker.header.frame_id = self.visualize_frame
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
    
    def create_text_marker(self, marker_id, x, y, z, new_bbox_check, id, label, score, relative_position, current_time):
        marker = Marker()
        marker.header.frame_id = self.visualize_frame
        marker.header.stamp = current_time.to_msg()
        marker.ns = "object_labels"
        marker.id = marker_id
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD

        marker.pose.position = Point(x=float(x), y=float(y), z=float(z))
        marker.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

        marker.scale.z = 0.5
        marker.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)

        bbox_state = "Fix > " if new_bbox_check == 0 else "Updating > "
        
        if int(label) == 0 and relative_position:  # boat일 경우 상대 위치 추가
            marker.text = f"{bbox_state}{self.class_names[int(label)]}{id}: {score:.2f} ({relative_position})"
        else:
            marker.text = f"{bbox_state}{self.class_names[int(label)]}{id}: {score:.2f}"

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

    def add_rotation_to_tf(self, original_rotation, rotation_to_add):
        # ROS Quaternion을 리스트로 변환
        original_quat = [original_rotation.w, original_rotation.x, original_rotation.y, original_rotation.z]
        add_quat = [rotation_to_add.w, rotation_to_add.x, rotation_to_add.y, rotation_to_add.z]

        # 쿼터니언 곱셈 (회전 추가)
        new_quat = qmult(original_quat, add_quat)

        # 결과를 ROS Quaternion 메시지로 변환
        return Quaternion(x=new_quat[1], y=new_quat[2], z=new_quat[3], w=new_quat[0])
    

def main(args=None):
    rclpy.init(args=args)
    marker_and_parking_point_visualizer = MarkerAndParkingPointVisualizer()
    
    try:
        rclpy.spin(marker_and_parking_point_visualizer)
    except KeyboardInterrupt:
        pass
    finally:
        marker_and_parking_point_visualizer.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()