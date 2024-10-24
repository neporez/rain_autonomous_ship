// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from det_msgs:msg/ClusteredDetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__STRUCT_H_
#define DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'bboxes'
// Member 'labels'
// Member 'scores'
// Member 'new_bbox_check'
// Member 'id'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.h"

/// Struct defined in msg/ClusteredDetectedObjects in the package det_msgs.
typedef struct det_msgs__msg__ClusteredDetectedObjects
{
  rosidl_runtime_c__float__Sequence bboxes;
  uint32_t bboxes_num;
  rosidl_runtime_c__int32__Sequence labels;
  rosidl_runtime_c__float__Sequence scores;
  /// 0인 경우는 업데이트가 안되는 중, 1인 경우는 업데이트 되는 중
  rosidl_runtime_c__int32__Sequence new_bbox_check;
  /// 바운딩 박스의 고유 아이디
  rosidl_runtime_c__int32__Sequence id;
  /// 메세지 받은 시점의 로컬 맵 상의 위치
  geometry_msgs__msg__Pose pose;
} det_msgs__msg__ClusteredDetectedObjects;

// Struct for a sequence of det_msgs__msg__ClusteredDetectedObjects.
typedef struct det_msgs__msg__ClusteredDetectedObjects__Sequence
{
  det_msgs__msg__ClusteredDetectedObjects * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} det_msgs__msg__ClusteredDetectedObjects__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__STRUCT_H_
