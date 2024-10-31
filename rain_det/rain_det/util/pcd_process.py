import numpy as np
from sensor_msgs_py import point_cloud2 as pc2

def point_range_filter(pts, point_range=[-69.12, -69.12, -3.0, 69.12, 69.12, 5.0]):
    flag_x_low = pts[:, 0] > point_range[0]
    flag_y_low = pts[:, 1] > point_range[1]
    flag_z_low = pts[:, 2] > point_range[2]
    flag_x_high = pts[:, 0] < point_range[3]
    flag_y_high = pts[:, 1] < point_range[4]
    flag_z_high = pts[:, 2] < point_range[5]
    keep_mask = flag_x_low & flag_y_low & flag_z_low & flag_x_high & flag_y_high & flag_z_high
    pts = pts[keep_mask]
    return pts 


def pointcloud2_to_array(cloud_msg):
    pc = pc2.read_points(cloud_msg, field_names=("x", "y", "z", "intensity"), skip_nans=True)
    dtype = np.dtype([('x', np.float32), ('y', np.float32), ('z', np.float32), ('intensity', np.float32)])
    points_numpy = np.fromiter(pc, dtype=dtype)
    return np.stack([points_numpy['x'], points_numpy['y'], points_numpy['z'], points_numpy['intensity']], axis=-1)
