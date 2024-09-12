import numpy as np
from collections import deque
import matplotlib.pyplot as plt

class ParkingPointGenerator:
    def __init__(self):
        self._result = None

    def generate_points(self, p1, p2, target_bar, bar_length, bar_distance, point_distance):
        self._result = self._calculate_points(p1, p2, target_bar, bar_length, bar_distance, point_distance)
        return self._result

    def get_result(self):
        return self._result

    def _calculate_angle(self, p1, p2):
        return np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))

    def _rotate_point(self, point, center, angle_deg):
        angle_rad = np.radians(angle_deg)
        cos_theta, sin_theta = np.cos(angle_rad), np.sin(angle_rad)
        x, y = point[0] - center[0], point[1] - center[1]
        new_x = x * cos_theta - y * sin_theta + center[0]
        new_y = x * sin_theta + y * cos_theta + center[1]
        return (new_x, new_y)

    def _calculate_perpendicular_points(self, p1, p2, distance):
        angle = self._calculate_angle(p1, p2)
        left_angle, right_angle = angle + 90, angle - 90
        left_point = (p1[0] + distance * np.cos(np.radians(left_angle)),
                      p1[1] + distance * np.sin(np.radians(left_angle)))
        right_point = (p1[0] + distance * np.cos(np.radians(right_angle)),
                       p1[1] + distance * np.sin(np.radians(right_angle)))
        return left_point, right_point

    def _calculate_end_point(self, start_point, angle_deg, length):
        return (start_point[0] + length * np.cos(np.radians(angle_deg)),
                start_point[1] + length * np.sin(np.radians(angle_deg)))

    def _distance_to_line(self, point, line_start, line_end):
        line_vec = np.array(line_end) - np.array(line_start)
        point_vec = np.array(point) - np.array(line_start)
        line_len = np.linalg.norm(line_vec)
        line_unitvec = line_vec / line_len
        point_vec_scaled = point_vec / line_len
        t = np.dot(line_unitvec, point_vec_scaled)
        if t < 0.0:
            t = 0.0
        elif t > 1.0:
            t = 1.0
        nearest = line_start + t * line_vec
        dist = np.linalg.norm(nearest - point)
        return dist

    def _find_rotation_angle(self, p1, p2, distance, bar_length, target_bar):
        base_angle = self._calculate_angle(p1, p2)
        p1_left, p1_right = self._calculate_perpendicular_points(p1, p2, distance)

        def rotate_and_check(angle):
            rotated_left = self._rotate_point(p1_left, p1, angle)
            rotated_right = self._rotate_point(p1_right, p1, angle)
           
            left_end = self._calculate_end_point(rotated_left, base_angle + angle, bar_length)
            right_end = self._calculate_end_point(rotated_right, base_angle + angle, bar_length)
           
            if target_bar == 'left':
                return self._distance_to_line(p2, rotated_left, left_end)
            else:  # right
                return self._distance_to_line(p2, rotated_right, right_end)

        left, right = -180, 180
        for _ in range(100):
            mid = (left + right) / 2
            if rotate_and_check(mid) < rotate_and_check(mid + 0.1):
                right = mid
            else:
                left = mid
            if right - left < 0.1:
                break

        best_angle = (left + right) / 2
        return best_angle

    def _calculate_p2_oppose(self, p1, p2, p1_left, p1_right, target_bar):
        if target_bar == 'left':
            vec = np.array(p2) - np.array(p1_left)
            p2_oppose = np.array(p1_right) + vec
        else:
            vec = np.array(p2) - np.array(p1_right)
            p2_oppose = np.array(p1_left) + vec
        return tuple(p2_oppose)

    def _generate_additional_points(self, start_point, end_point, p2, p2_oppose, point_distance):
        direction = np.array(end_point) - np.array(start_point)
        unit_direction = direction / np.linalg.norm(direction)
        bar_length = np.linalg.norm(direction)
       
        points = deque()
        opposite_points = deque()
       
        # Generate points for the target bar
        current_point = np.array(p2, dtype=float)
        while 0 <= np.dot(current_point - np.array(start_point), unit_direction) <= bar_length:
            points.append(tuple(current_point))
            current_point = current_point + unit_direction * point_distance
       
        current_point = np.array(p2, dtype=float) - unit_direction * point_distance
       
        while 0 <= np.dot(current_point - np.array(start_point), unit_direction) <= bar_length:
            points.appendleft(tuple(current_point))
            current_point = current_point - unit_direction * point_distance
       
        # Generate points for the opposite bar
        current_point = np.array(p2_oppose, dtype=float)
        while 0 <= np.dot(current_point - np.array(start_point), unit_direction) <= bar_length:
            opposite_points.append(tuple(current_point))
            current_point = current_point + unit_direction * point_distance
       
        current_point = np.array(p2_oppose, dtype=float) - unit_direction * point_distance
        while 0 <= np.dot(current_point - np.array(start_point), unit_direction) <= bar_length:
            opposite_points.appendleft(tuple(current_point))
            current_point = current_point - unit_direction * point_distance
       
        return list(points), list(opposite_points)

    def _calculate_points(self, p1, p2, target_bar, bar_length, bar_distance, point_distance):
        rotation_angle = self._find_rotation_angle(p1, p2, bar_distance, bar_length, target_bar)
       
        base_angle = self._calculate_angle(p1, p2)
        p1_left, p1_right = self._calculate_perpendicular_points(p1, p2, bar_distance)
       
        # Rotate points
        p1_left = self._rotate_point(p1_left, p1, rotation_angle)
        p1_right = self._rotate_point(p1_right, p1, rotation_angle)
       
        # Calculate end points
        p1_left_end = self._calculate_end_point(p1_left, base_angle + rotation_angle, bar_length)
        p1_right_end = self._calculate_end_point(p1_right, base_angle + rotation_angle, bar_length)
       
        # Calculate p2_oppose
        p2_oppose = self._calculate_p2_oppose(p1, p2, p1_left, p1_right, target_bar)
       
        if target_bar == 'left':
            target_start, target_end = p1_left, p1_left_end
            opposite_start, opposite_end = p1_right, p1_right_end
        else:
            target_start, target_end = p1_right, p1_right_end
            opposite_start, opposite_end = p1_left, p1_left_end
       
        # Generate additional points
        target_points, opposite_points = self._generate_additional_points(
            target_start, target_end, p2, p2_oppose, point_distance)
     
        if target_bar == 'left':
            all_points = deque(target_points[::-1][:-1])
            all_points.extend(opposite_points[::-1][:-1])
        else:
            all_points = deque(opposite_points[::-1][:-1])
            all_points.extend(target_points[::-1][:-1])
       
        return list(all_points)

# 사용 예시
generator = ParkingPointGenerator()
p1 = (30, 20)
p2 = (24, 16)
target_bar = 'left'
bar_length = 35.0
bar_distance = 2.0
point_distance = 5.0

result = generator.generate_points(p1, p2, target_bar, bar_length, bar_distance, point_distance)
print("Generated points:", result)