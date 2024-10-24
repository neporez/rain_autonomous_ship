// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from det_msgs:msg/DetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__STRUCT_H_
#define DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__STRUCT_H_

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
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/DetectedObjects in the package det_msgs.
/**
  * 모델의 결과 값, bboxes는 reshape를 통해 (bboxes_num,7)의 값을 1차원 배열로 저장
 */
typedef struct det_msgs__msg__DetectedObjects
{
  rosidl_runtime_c__float__Sequence bboxes;
  /// 바운딩 박스의 갯수
  uint32_t bboxes_num;
  /// 각 바운딩 박스의 라벨값
  rosidl_runtime_c__int32__Sequence labels;
  /// 각 바운딩 박스의 신뢰도
  rosidl_runtime_c__float__Sequence scores;
} det_msgs__msg__DetectedObjects;

// Struct for a sequence of det_msgs__msg__DetectedObjects.
typedef struct det_msgs__msg__DetectedObjects__Sequence
{
  det_msgs__msg__DetectedObjects * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} det_msgs__msg__DetectedObjects__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__STRUCT_H_
