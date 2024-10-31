# 모델의 결과 값, bboxes는 reshape를 통해 (bboxes_num,7)의 값을 1차원 배열로 저장
float32[] bboxes 

# 바운딩 박스의 갯수
uint32 bboxes_num

# 각 바운딩 박스의 라벨값 
int32[] labels

# 각 바운딩 박스의 신뢰도
float32[] scores