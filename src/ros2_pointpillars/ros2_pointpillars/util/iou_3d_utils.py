# iou_3d_utils.py

import numpy as np
from transforms3d.euler import quat2euler

def calculate_3d_iou(marker1, marker2):
    # 마커에서 필요한 정보 추출
    center1, size1, orientation1 = marker1.pose.position, marker1.scale, marker1.pose.orientation
    center2, size2, orientation2 = marker2.pose.position, marker2.scale, marker2.pose.orientation

    # 회전 행렬 계산
    _, _, yaw1 = quat2euler([orientation1.w, orientation1.x, orientation1.y, orientation1.z])
    _, _, yaw2 = quat2euler([orientation2.w, orientation2.x, orientation2.y, orientation2.z])
    
    # 바운딩 박스의 코너 점 계산
    corners1 = get_bbox_corners(center1, size1, yaw1)
    corners2 = get_bbox_corners(center2, size2, yaw2)

    # 교집합 볼륨 계산
    inter_vol = compute_intersection(corners1, corners2)

    # 각 바운딩 박스의 볼륨 계산
    vol1 = size1.x * size1.y * size1.z
    vol2 = size2.x * size2.y * size2.z

    # IoU 계산
    union_vol = vol1 + vol2 - inter_vol
    iou = inter_vol / union_vol if union_vol > 0 else 0

    return iou

def get_bbox_corners(center, size, yaw):
    # 바운딩 박스의 코너 점 계산
    c = np.cos(yaw)
    s = np.sin(yaw)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    
    l, w, h = size.x / 2, size.y / 2, size.z / 2
    x_corners = [-l, l, l, -l, -l, l, l, -l]
    y_corners = [-w, -w, w, w, -w, -w, w, w]
    z_corners = [-h, -h, -h, -h, h, h, h, h]
    corners = np.dot(R, np.vstack([x_corners, y_corners, z_corners]))
    corners += np.array([center.x, center.y, center.z])[:, np.newaxis]
    return corners.T

def compute_intersection(corners1, corners2):
    # 두 바운딩 박스의 교집합 볼륨 계산
    # 이 함수는 복잡한 기하학적 계산을 포함합니다
    # 여기서는 간단한 근사치 방법을 사용합니다
    
    # 각 축에 대한 투영의 교집합 계산
    min_x = max(np.min(corners1[:, 0]), np.min(corners2[:, 0]))
    max_x = min(np.max(corners1[:, 0]), np.max(corners2[:, 0]))
    min_y = max(np.min(corners1[:, 1]), np.min(corners2[:, 1]))
    max_y = min(np.max(corners1[:, 1]), np.max(corners2[:, 1]))
    min_z = max(np.min(corners1[:, 2]), np.min(corners2[:, 2]))
    max_z = min(np.max(corners1[:, 2]), np.max(corners2[:, 2]))

    # 교집합 볼륨 계산
    intersection = max(0, max_x - min_x) * max(0, max_y - min_y) * max(0, max_z - min_z)
    return intersection