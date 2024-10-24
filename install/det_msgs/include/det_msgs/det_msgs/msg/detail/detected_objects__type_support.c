// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from det_msgs:msg/DetectedObjects.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "det_msgs/msg/detail/detected_objects__rosidl_typesupport_introspection_c.h"
#include "det_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "det_msgs/msg/detail/detected_objects__functions.h"
#include "det_msgs/msg/detail/detected_objects__struct.h"


// Include directives for member types
// Member `bboxes`
// Member `labels`
// Member `scores`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  det_msgs__msg__DetectedObjects__init(message_memory);
}

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_fini_function(void * message_memory)
{
  det_msgs__msg__DetectedObjects__fini(message_memory);
}

size_t det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__size_function__DetectedObjects__bboxes(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__bboxes(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__bboxes(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__fetch_function__DetectedObjects__bboxes(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__bboxes(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__assign_function__DetectedObjects__bboxes(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__bboxes(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__resize_function__DetectedObjects__bboxes(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__size_function__DetectedObjects__labels(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__labels(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__labels(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__fetch_function__DetectedObjects__labels(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__labels(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__assign_function__DetectedObjects__labels(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__labels(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__resize_function__DetectedObjects__labels(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

size_t det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__size_function__DetectedObjects__scores(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__scores(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__scores(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__fetch_function__DetectedObjects__scores(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__scores(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__assign_function__DetectedObjects__scores(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__scores(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__resize_function__DetectedObjects__scores(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_member_array[4] = {
  {
    "bboxes",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs__msg__DetectedObjects, bboxes),  // bytes offset in struct
    NULL,  // default value
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__size_function__DetectedObjects__bboxes,  // size() function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__bboxes,  // get_const(index) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__bboxes,  // get(index) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__fetch_function__DetectedObjects__bboxes,  // fetch(index, &value) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__assign_function__DetectedObjects__bboxes,  // assign(index, value) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__resize_function__DetectedObjects__bboxes  // resize(index) function pointer
  },
  {
    "bboxes_num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs__msg__DetectedObjects, bboxes_num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "labels",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs__msg__DetectedObjects, labels),  // bytes offset in struct
    NULL,  // default value
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__size_function__DetectedObjects__labels,  // size() function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__labels,  // get_const(index) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__labels,  // get(index) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__fetch_function__DetectedObjects__labels,  // fetch(index, &value) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__assign_function__DetectedObjects__labels,  // assign(index, value) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__resize_function__DetectedObjects__labels  // resize(index) function pointer
  },
  {
    "scores",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs__msg__DetectedObjects, scores),  // bytes offset in struct
    NULL,  // default value
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__size_function__DetectedObjects__scores,  // size() function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_const_function__DetectedObjects__scores,  // get_const(index) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__get_function__DetectedObjects__scores,  // get(index) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__fetch_function__DetectedObjects__scores,  // fetch(index, &value) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__assign_function__DetectedObjects__scores,  // assign(index, value) function pointer
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__resize_function__DetectedObjects__scores  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_members = {
  "det_msgs__msg",  // message namespace
  "DetectedObjects",  // message name
  4,  // number of fields
  sizeof(det_msgs__msg__DetectedObjects),
  det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_member_array,  // message members
  det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_init_function,  // function to initialize message memory (memory has to be allocated)
  det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_type_support_handle = {
  0,
  &det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_det_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, det_msgs, msg, DetectedObjects)() {
  if (!det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_type_support_handle.typesupport_identifier) {
    det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &det_msgs__msg__DetectedObjects__rosidl_typesupport_introspection_c__DetectedObjects_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
