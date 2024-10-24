import numpy as np
from sklearn.cluster import DBSCAN
from scipy.spatial.transform import Rotation
from collections import deque
from transforms3d.euler import euler2quat, quat2euler
from transforms3d.quaternions import quat2mat, qmult

def calculate_xy_distance(bbox1, bbox2):
    """Calculate Euclidean distance between two bounding boxes in XY plane."""
    return np.linalg.norm(bbox1[:2] - bbox2[:2])

class BoundingBoxDBSCAN:
    def __init__(self, eps=0.5, min_samples=3, queue_size=100, tracking_queue_size=100, distance_threshold=2.0, update_weight=0.1):
        self.__eps = eps
        self.__min_samples = min_samples
        self.__queue_size = queue_size
        self.__tracking_queue_size = tracking_queue_size
        self.__distance_threshold = distance_threshold
        self.__update_weight = update_weight

        self.__current_pose = None
        self.__dbscan = DBSCAN(eps=self.__eps, min_samples=self.__min_samples)
        self.__bbox_queue = deque(maxlen=self.__queue_size)
        self.__tracking_queue = deque(maxlen=self.__tracking_queue_size)
        self.__next_id = 0

        self.__NEW_BBOX_CHECK_TRUE = 1
        self.__NEW_BBOX_CHECK_FALSE = 0

    def clustering(self, model_result, current_pose):
        self.__current_pose = current_pose
        lidar_bboxes, labels, scores = model_result
        transformed_bboxes = self.__transform_bboxes_to_ndt(lidar_bboxes)
        filtered_data = [(bbox, label, score) for bbox, label, score in zip(transformed_bboxes, labels, scores) if score >= 0.8]

        if filtered_data:
            filtered_bboxes, filtered_labels, filtered_scores = zip(*filtered_data)
            self.__bbox_queue.append([filtered_bboxes, filtered_labels, filtered_scores, self.__NEW_BBOX_CHECK_TRUE])

        clustered_bboxes = self.__perform_dbscan_clustering()
        tracked_bboxes = self.__update_tracking_distance(clustered_bboxes)
        return tracked_bboxes

    def __transform_bboxes_to_ndt(self, bboxes):
        transformed_bboxes = []
        current_quat = np.array([
            self.__current_pose.orientation.w,
            self.__current_pose.orientation.x,
            self.__current_pose.orientation.y,
            self.__current_pose.orientation.z
        ])
        current_rot_mat = quat2mat(current_quat)
        current_euler = quat2euler(current_quat)

        for bbox in bboxes:
            x, y, z, w, l, h, yaw = bbox
            
            local_pos = np.array([x, y, z])
            global_pos = np.dot(current_rot_mat, local_pos) + np.array([
                self.__current_pose.position.x,
                self.__current_pose.position.y,
                self.__current_pose.position.z
            ])

            global_yaw = -yaw + current_euler[2]
            global_yaw = (global_yaw + np.pi) % (2 * np.pi) - np.pi

            transformed_bboxes.append(np.array([global_pos[0], global_pos[1], global_pos[2], w, l, h, global_yaw]))

        return transformed_bboxes

    def __perform_dbscan_clustering(self):
        all_bboxes = []
        for i, (bboxes, labels, scores, new_bbox_check) in enumerate(self.__bbox_queue):
            all_bboxes.extend([(np.array(bbox), label, score, new_bbox_check) for bbox, label, score in zip(bboxes, labels, scores)])
            if new_bbox_check == self.__NEW_BBOX_CHECK_TRUE :
                self.__bbox_queue[i][-1] = self.__NEW_BBOX_CHECK_FALSE

        if not all_bboxes:
            return []

        X = np.array([bbox[:2] for bbox, _, _, _ in all_bboxes])
        clusters = self.__dbscan.fit_predict(X)

        clustered_bboxes = []
        for cluster_id in set(clusters):
            if cluster_id == -1:
                continue
            
            cluster_bboxes = [all_bboxes[i] for i in range(len(all_bboxes)) if clusters[i] == cluster_id]
            avg_bbox = np.mean([bbox[:6] for bbox, _, _, _ in cluster_bboxes], axis=0)
            yaw_angles = [bbox[6] for bbox, _, _, _ in cluster_bboxes]
            avg_yaw = np.arctan2(np.mean(np.sin(yaw_angles)), np.mean(np.cos(yaw_angles)))
            avg_bbox = np.append(avg_bbox, avg_yaw)
            avg_label = max(set([label for _, label, _, _ in cluster_bboxes]), key=[label for _, label, _, _ in cluster_bboxes].count)
            avg_score = np.mean([score for _, _, score, _ in cluster_bboxes])

            avg_update_check = np.mean([new_bbox_check for _, _, _, new_bbox_check in cluster_bboxes])
            
            clustered_bboxes.append((avg_bbox, avg_label, avg_score, avg_update_check))

        return clustered_bboxes

    def __update_tracking_distance(self, clustered_bboxes):
        if not self.__tracking_queue:
            # Initialize tracking queue if empty
            for bbox, label, score, new_bbox_check in clustered_bboxes:
                self.__tracking_queue.append((np.array(bbox), label, score, new_bbox_check ,self.__next_id))
                self.__next_id += 1
            return list(self.__tracking_queue)
    
        new_tracking_queue = []
        unmatched_clustered = list(range(len(clustered_bboxes)))

        for tracked_bbox, tracked_label, tracked_score, new_bbox_check ,tracked_id in self.__tracking_queue:
            best_match = None
            min_distance = float('inf')

            for i, (clustered_bbox, clustered_label, clustered_score, _) in enumerate(clustered_bboxes):
                if i in unmatched_clustered:
                    distance = calculate_xy_distance(tracked_bbox, clustered_bbox)
                    if distance < self.__distance_threshold and distance < min_distance:
                        min_distance = distance
                        best_match = i

            if best_match is not None:
                clustered_bbox, clustered_label, clustered_score, new_bbox_check = clustered_bboxes[best_match]
                updated_bbox = self.__update_weight * tracked_bbox + (1 - self.__update_weight) * np.array(clustered_bbox)
                new_tracking_queue.append((updated_bbox, clustered_label, clustered_score, new_bbox_check ,tracked_id))
                unmatched_clustered.remove(best_match)
            else : 
                new_tracking_queue.append((tracked_bbox, tracked_label, tracked_score, self.__NEW_BBOX_CHECK_FALSE, tracked_id))

        # Add new unmatched clustered bboxes
        for i in unmatched_clustered:
            clustered_bbox, clustered_label, clustered_score, new_bbox_check = clustered_bboxes[i]
            new_tracking_queue.append((np.array(clustered_bbox), clustered_label, clustered_score, new_bbox_check ,self.__next_id))
            self.__next_id += 1

        self.__tracking_queue = deque(new_tracking_queue, maxlen=self.__tracking_queue_size)
        return list(self.__tracking_queue)