import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Point, Quaternion, Vector3
from visualization_msgs.msg import Marker, MarkerArray
from sensor_msgs_py import point_cloud2 as pc2
from transforms3d.euler import euler2quat

import numpy as np
import torch
import sys
import os
import math
import time

import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit

model_path = "/home/rain/PointPillars"
sys.path.append(model_path)

from utils import keep_bbox_from_lidar_range
from model import PointPillarsCore, PointPillarsPre, PointPillarsPos

cuda.init()
device = cuda.Device(0)
cuda_driver_context = device.make_context()

class HostDeviceMem(object):
    def __init__(self, host_mem, device_mem):
        self.host = host_mem
        self.device = device_mem

    def __str__(self):
        return "Host:\n" + str(self.host) + "\nDevice:\n" + str(self.device)

    def __repr__(self):
        return self.__str__()

class PointCloudProcessor(Node):
    def __init__(self):
        super().__init__('pointcloud_processor')
        
        self.declare_parameter('trt_engine', '/home/rain/PointPillars/pretrained/model.trt')

        self.subscription = self.create_subscription(
            PointCloud2,
            '/point_cloud',
            self.pointcloud_callback,
            10)

        # self.subscription = self.create_subscription(
        #     PointCloud2,
        #     '/livox/lidar',
        #     self.pointcloud_callback,
        #     10)

        
        self.bbox_publisher = self.create_publisher(MarkerArray, 'bounding_boxes', 10)

        self.CLASSES = {
            'Pedestrian': 0, 
            'Cyclist': 1, 
            'Car': 2
        }
        self.class_names = list(self.CLASSES.keys())

        self.pcd_limit_range = np.array([-69.12, -69.12, -3, 69.12, 69.12, 1], dtype=np.float32)
        
        self.model_pre = PointPillarsPre().cuda()

        self.trt_logger = trt.Logger(trt.Logger.WARNING)
        self.trt_runtime = trt.Runtime(self.trt_logger)
        self.engine = self.get_parameter('trt_engine').get_parameter_value().string_value

        if not self.engine:
            self.get_logger().error('trt_engine parameter is not set!')
            return

        self.engine = self.load_engine(self.trt_runtime, self.engine)

        self.context_trt = self.engine.create_execution_context()

        self.max_num_pillars = 40000
        self.inputs, self.outputs, self.bindings, self.stream = self.allocate_buffers(self.max_num_pillars)

        self.model_post = PointPillarsPos(nclasses=len(self.CLASSES)).cuda()
        
        self.model_pre.eval()
        self.model_post.eval()

        self.prev_markers = {}
        self.marker_lifetime = 0.2

    def load_engine(self, trt_runtime, engine_path):
        with open(engine_path, 'rb') as f:
            engine_data = f.read()
        engine = trt_runtime.deserialize_cuda_engine(engine_data)
        return engine

    def allocate_buffers(self, max_num_pillars):
        inputs = []
        outputs = []
        bindings = []
        stream = cuda.Stream()

        for binding in range(self.engine.num_io_tensors):
            tensor_name = self.engine.get_tensor_name(binding)
            shape = self.engine.get_tensor_shape(tensor_name)

            if -1 in shape:
                if 'input_pillars' in tensor_name:
                    shape = (max_num_pillars, 32, 4)
                elif 'input_coors_batch' in tensor_name:
                    shape = (max_num_pillars, 4)
                elif 'input_npoints_per_pillar' in tensor_name:
                    shape = (max_num_pillars,)
                else:
                    shape = self.engine.get_tensor_profile_shape(tensor_name, 0)[2]

            size = trt.volume(shape)
            dtype = trt.nptype(self.engine.get_tensor_dtype(tensor_name))

            host_mem = cuda.pagelocked_empty(size, dtype)
            device_mem = cuda.mem_alloc(host_mem.nbytes)

            bindings.append(int(device_mem))

            if self.engine.get_tensor_mode(tensor_name) == trt.TensorIOMode.INPUT:
                inputs.append(HostDeviceMem(host_mem, device_mem))
            else:
                outputs.append(HostDeviceMem(host_mem, device_mem))

        return inputs, outputs, bindings, stream

    def do_inference(self, context, bindings, inputs, outputs, stream):
        [cuda.memcpy_htod_async(inp.device, inp.host, stream) for inp in inputs]
        context.execute_async_v2(bindings=bindings, stream_handle=stream.handle)
        [cuda.memcpy_dtoh_async(out.host, out.device, stream) for out in outputs]
        stream.synchronize()
        return [out.host for out in outputs]

    def point_range_filter(self, pts, point_range=[0, -39.68, -3, 69.12, 39.68, 1]):
        flag_x_low = pts[:, 0] > point_range[0]
        flag_y_low = pts[:, 1] > point_range[1]
        flag_z_low = pts[:, 2] > point_range[2]
        flag_x_high = pts[:, 0] < point_range[3]
        flag_y_high = pts[:, 1] < point_range[4]
        flag_z_high = pts[:, 2] < point_range[5]
        keep_mask = flag_x_low & flag_y_low & flag_z_low & flag_x_high & flag_y_high & flag_z_high
        pts = pts[keep_mask]
        return pts 

    def pointcloud_callback(self, msg):
        points = self.point_range_filter(self.pointcloud2_to_array(msg))
        self.process_pointcloud(points)

    def process_pointcloud(self, points):

        
        cuda_driver_context.push()
        pc_torch = torch.from_numpy(points).cuda()

        pre_time = time.time()

        with torch.no_grad():
            pillars, coors_batch, npoints_per_pillar = self.model_pre(batched_pts=[pc_torch])

            num_pillars = pillars.shape[0]

        for i, inp in enumerate(self.inputs):
            if i == 0:
                data = pillars.cpu().numpy().astype(np.float32)
            elif i == 1:
                data = coors_batch.cpu().numpy().astype(np.int32)
            elif i == 2:
                data = npoints_per_pillar.cpu().numpy().astype(np.int32)
            else:
                raise ValueError(f"Unexpected input index: {i}")

            if data.dtype != inp.host.dtype:
                print(f"Warning: Data type mismatch for input {i}. Expected {inp.host.dtype}, got {data.dtype}")
                data = data.astype(inp.host.dtype)

            np.copyto(inp.host[:data.size], data.ravel())

        self.context_trt.set_binding_shape(0, (num_pillars, 32, 4))
        self.context_trt.set_binding_shape(1, (num_pillars, 4))
        self.context_trt.set_binding_shape(2, (num_pillars,))

        trt_outputs = self.do_inference(self.context_trt, self.bindings, self.inputs, self.outputs, self.stream)
        

        result = [torch.from_numpy(trt_outputs[0].reshape(-1, 11)).cuda()]


        try:
            result_filter = self.model_post(result)[0]
        except:
            print("inference failed")
            return
        print("Model inference time:", time.time() - pre_time)

        cuda_driver_context.pop()

        result_filter = keep_bbox_from_lidar_range(result_filter, self.pcd_limit_range)
        lidar_bboxes = result_filter['lidar_bboxes']
        labels, scores = result_filter['labels'], result_filter['scores']

        bbox_msg = self.create_bbox_markers(lidar_bboxes, labels, scores)
        self.bbox_publisher.publish(bbox_msg)

    def pointcloud2_to_array(self, cloud_msg):
        pc = pc2.read_points(cloud_msg, field_names=("x", "y", "z", "intensity"), skip_nans=True)
        dtype = np.dtype([('x', np.float32), ('y', np.float32), ('z', np.float32), ('intensity', np.float32)])
        points_numpy = np.fromiter(pc, dtype=dtype)
        return np.stack([points_numpy['x'], points_numpy['y'], points_numpy['z'], points_numpy['intensity']], axis=-1)

    def create_bbox_markers(self, bboxes, labels, scores):
        marker_array = MarkerArray()
        current_markers = {}

        for i, (bbox, label, score) in enumerate(zip(bboxes, labels, scores)):
            if score < 0.6:
                continue
            box_marker = self.create_box_marker(i, *bbox, label)
            text_marker = self.create_text_marker(i, bbox[0], bbox[1], bbox[2] + bbox[3], label, score)
            
            marker_array.markers.extend([box_marker, text_marker])
            current_markers[i] = box_marker
            current_markers[f"text_{i}"] = text_marker

        for prev_id, prev_marker in self.prev_markers.items():
            if prev_id not in current_markers:
                prev_marker.action = Marker.DELETE
                marker_array.markers.append(prev_marker)

        self.prev_markers = current_markers
        return marker_array

    def create_box_marker(self, marker_id, x, y, z, l, w, h, yaw, label):
        marker = Marker()
        marker.header.frame_id = "map"
        #marker.header.frame_id = "livox_frame"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "bounding_boxes"
        marker.id = marker_id
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.pose.position = Point(x=float(x), y=float(y), z=float(z + h/2))
        q = euler2quat(0, 0, float(-yaw))
        marker.pose.orientation = Quaternion(x=float(q[1]), y=float(q[2]), z=float(q[3]), w=float(q[0]))
        marker.scale = Vector3(x=float(l), y=float(w), z=float(h))
        marker.color = self.get_color_for_label(label)
        marker.lifetime = rclpy.duration.Duration(seconds=self.marker_lifetime).to_msg()
        return marker

    def create_text_marker(self, marker_id, x, y, z, label, score):
        marker = Marker()
        marker.header.frame_id = "map"
        #marker.header.frame_id = "livox_frame"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "object_labels"
        marker.id = marker_id
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD
        marker.pose.position = Point(x=float(x), y=float(y), z=float(z + 0.5))
        marker.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        marker.scale.z = 0.5
        marker.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
        marker.text = f"{self.class_names[int(label)]}: {score:.2f}"
        marker.lifetime = rclpy.duration.Duration(seconds=self.marker_lifetime).to_msg()
        return marker

    def get_color_for_label(self, label):
        colors = [
            ColorRGBA(r=1.0, g=0.0, b=0.0, a=0.3),  # Pedestrian: Red
            ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.3),  # Cyclist: Green
            ColorRGBA(r=0.0, g=0.0, b=1.0, a=0.3),  # Car: Blue
        ]
        return colors[int(label)]

def main(args=None):
    rclpy.init(args=args)
    pointcloud_processor = PointCloudProcessor()
    
    try:
        while rclpy.ok():
            rclpy.spin_once(pointcloud_processor, timeout_sec=0.05)
    except KeyboardInterrupt:
        pass
    finally:
        pointcloud_processor.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()