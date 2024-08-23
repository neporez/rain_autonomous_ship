import numpy as np
from sklearn.cluster import DBSCAN
from scipy.spatial.transform import Rotation
from collections import deque
from transforms3d.euler import euler2quat, quat2euler
from transforms3d.quaternions import quat2mat, qmult
from shapely.geometry import Polygon

def calculate_3d_iou(bbox1, bbox2):
    """
    Calculate 3D IoU between two bounding boxes.
    bbox1, bbox2: [x, y, z, w, l, h, theta]
    """
    # Ensure inputs are numpy arrays
    bbox1 = np.array(bbox1)
    bbox2 = np.array(bbox2)

    # 1. height overlap
    z1, z2 = bbox1[2], bbox2[2]
    h1, h2 = bbox1[5], bbox2[5]
    bottom = max(z1, z2)
    top = min(z1 + h1, z2 + h2)
    height_overlap = max(0, top - bottom)

    # 2. bev overlap
    corners1 = get_bbox_corners(bbox1)
    corners2 = get_bbox_corners(bbox2)
    bev_overlap = compute_bev_intersection(corners1, corners2)

    # 3. overlap and volume
    overlap = height_overlap * bev_overlap
    volume1 = bbox1[3] * bbox1[4] * bbox1[5]
    volume2 = bbox2[3] * bbox2[4] * bbox2[5]
    volume = volume1 + volume2

    # 4. iou
    iou = overlap / (volume - overlap + 1e-8)

    return iou

def get_bbox_corners(bbox):
    """Get corners of 3D bounding box in BEV."""
    x, y, _, w, l, _, yaw = bbox
    cos_yaw = np.cos(yaw)
    sin_yaw = np.sin(yaw)
    
    x_corners = np.array([l/2, l/2, -l/2, -l/2])
    y_corners = np.array([w/2, -w/2, -w/2, w/2])
    
    rotated_x_corners = x + cos_yaw * x_corners + sin_yaw * y_corners
    rotated_y_corners = y - sin_yaw * x_corners + cos_yaw * y_corners
    
    return np.vstack([rotated_x_corners, rotated_y_corners]).T

def compute_bev_intersection(corners1, corners2):
    """Compute intersection area of two bounding boxes in BEV."""
    poly1 = Polygon(corners1)
    poly2 = Polygon(corners2)
    intersection = poly1.intersection(poly2)
    return intersection.area