import numpy as np

from sklearn.cluster import DBSCAN
from scipy.spatial.transform import Rotation

from collections import deque

from transforms3d.euler import euler2quat, quat2euler
from transforms3d.quaternions import quat2mat, qmult


class BoudingBoxDBSCAN():
    def __init__(self, eps=0.5, min_samples=3, queue_size=1000) :

        self.__eps = eps
        self.__min_samples = min_samples
        self.__queue_size = queue_size

        self.__current_pose = None


        self.__dbscan = DBSCAN(eps=self.__eps, min_samples=self.__min_samples)  # DBSCAN 파라미터 조정 필요
        self.__bbox_queue = deque(maxlen=self.__queue_size)  # 최근 1000개의 프레임 데이터를 저장

    def clustering(self, model_result, current_pose) :
        self.__current_pose = current_pose

        ### model_result : (lidar_bboxes, labels, scores)

        lidar_bboxes, labels, scores = model_result

        transformed_bboxes = self.__transform_bboxes_to_ndt(lidar_bboxes)

        filtered_data = [(bbox, label, score) for bbox, label, score in zip(transformed_bboxes, labels, scores) if score >= 0.7]


        if filtered_data:
            filtered_bboxes, filtered_labels, filtered_scores = zip(*filtered_data)
            self.__bbox_queue.append((filtered_bboxes, filtered_labels, filtered_scores))

        clustered_bboxes = self.perform_dbscan_clustering()

        return clustered_bboxes


    def __transform_bboxes_to_ndt(self, bboxes):
        transformed_bboxes = []
        current_quat = [
            self.__current_pose.orientation.w,
            self.__current_pose.orientation.x,
            self.__current_pose.orientation.y,
            self.__current_pose.orientation.z
        ]
        current_rot_mat = quat2mat(current_quat)
        current_euler = quat2euler(current_quat)

        for bbox in bboxes:
            x, y, z, l, w, h, yaw = bbox
            
            # 위치 변환
            local_pos = np.array([x, y, z])
            global_pos = np.dot(current_rot_mat, local_pos) + np.array([
                self.__current_pose.position.x,
                self.__current_pose.position.y,
                self.__current_pose.position.z
            ])

            # yaw 각도 변환
            # 로컬 yaw를 글로벌 yaw로 변환
            global_yaw = -yaw + current_euler[2]
            global_yaw = (global_yaw + np.pi) % (2 * np.pi) - np.pi  # -pi에서 pi 사이로 정규화

            transformed_bboxes.append([global_pos[0], global_pos[1], global_pos[2], l, w, h, global_yaw])

        return transformed_bboxes
    
    def perform_dbscan_clustering(self):
        all_bboxes = []
        for bboxes, labels, scores in self.__bbox_queue:
            all_bboxes.extend([(bbox, label, score) for bbox, label, score in zip(bboxes, labels, scores)])

        if not all_bboxes:
            return []

        # DBSCAN 클러스터링을 위한 데이터 준비
        X = np.array([bbox[:3] for bbox, _, _ in all_bboxes])  # x, y, z 좌표만 사용
        
        # DBSCAN 수행
        clusters = self.__dbscan.fit_predict(X)

        # 클러스터별로 평균 계산
        clustered_bboxes = []
        for cluster_id in set(clusters):
            if cluster_id == -1:  # 노이즈 포인트 무시
                continue
            
            cluster_bboxes = [all_bboxes[i] for i in range(len(all_bboxes)) if clusters[i] == cluster_id]
            
            # 위치와 크기의 평균 계산 (yaw 제외)
            avg_bbox = np.mean([bbox[:6] for bbox, _, _ in cluster_bboxes], axis=0)
            
            # yaw 각도 평균 계산 (원형 평균)
            yaw_angles = [bbox[6] for bbox, _, _ in cluster_bboxes]
            avg_yaw = np.arctan2(np.mean(np.sin(yaw_angles)), np.mean(np.cos(yaw_angles)))
            
            # 평균 yaw를 avg_bbox에 추가
            avg_bbox = np.append(avg_bbox, avg_yaw)
            
            avg_label = max(set([label for _, label, _ in cluster_bboxes]), key=[label for _, label, _ in cluster_bboxes].count)
            avg_score = np.mean([score for _, _, score in cluster_bboxes])
            
            # 객체 추적 및 ID 할당
            
            clustered_bboxes.append((avg_bbox, avg_label, avg_score))

        return clustered_bboxes