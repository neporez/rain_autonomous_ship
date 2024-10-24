// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from det_msgs:msg/ClusteredDetectedObjects.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "det_msgs/msg/detail/clustered_detected_objects__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace det_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void ClusteredDetectedObjects_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) det_msgs::msg::ClusteredDetectedObjects(_init);
}

void ClusteredDetectedObjects_fini_function(void * message_memory)
{
  auto typed_message = static_cast<det_msgs::msg::ClusteredDetectedObjects *>(message_memory);
  typed_message->~ClusteredDetectedObjects();
}

size_t size_function__ClusteredDetectedObjects__bboxes(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ClusteredDetectedObjects__bboxes(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__ClusteredDetectedObjects__bboxes(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__ClusteredDetectedObjects__bboxes(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__ClusteredDetectedObjects__bboxes(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__ClusteredDetectedObjects__bboxes(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__ClusteredDetectedObjects__bboxes(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__ClusteredDetectedObjects__bboxes(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ClusteredDetectedObjects__labels(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ClusteredDetectedObjects__labels(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__ClusteredDetectedObjects__labels(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__ClusteredDetectedObjects__labels(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__ClusteredDetectedObjects__labels(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__ClusteredDetectedObjects__labels(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__ClusteredDetectedObjects__labels(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__ClusteredDetectedObjects__labels(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ClusteredDetectedObjects__scores(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ClusteredDetectedObjects__scores(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__ClusteredDetectedObjects__scores(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__ClusteredDetectedObjects__scores(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__ClusteredDetectedObjects__scores(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__ClusteredDetectedObjects__scores(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__ClusteredDetectedObjects__scores(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__ClusteredDetectedObjects__scores(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ClusteredDetectedObjects__new_bbox_check(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ClusteredDetectedObjects__new_bbox_check(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__ClusteredDetectedObjects__new_bbox_check(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__ClusteredDetectedObjects__new_bbox_check(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__ClusteredDetectedObjects__new_bbox_check(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__ClusteredDetectedObjects__new_bbox_check(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__ClusteredDetectedObjects__new_bbox_check(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__ClusteredDetectedObjects__new_bbox_check(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ClusteredDetectedObjects__id(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ClusteredDetectedObjects__id(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__ClusteredDetectedObjects__id(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__ClusteredDetectedObjects__id(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__ClusteredDetectedObjects__id(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__ClusteredDetectedObjects__id(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__ClusteredDetectedObjects__id(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__ClusteredDetectedObjects__id(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ClusteredDetectedObjects_message_member_array[7] = {
  {
    "bboxes",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::ClusteredDetectedObjects, bboxes),  // bytes offset in struct
    nullptr,  // default value
    size_function__ClusteredDetectedObjects__bboxes,  // size() function pointer
    get_const_function__ClusteredDetectedObjects__bboxes,  // get_const(index) function pointer
    get_function__ClusteredDetectedObjects__bboxes,  // get(index) function pointer
    fetch_function__ClusteredDetectedObjects__bboxes,  // fetch(index, &value) function pointer
    assign_function__ClusteredDetectedObjects__bboxes,  // assign(index, value) function pointer
    resize_function__ClusteredDetectedObjects__bboxes  // resize(index) function pointer
  },
  {
    "bboxes_num",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::ClusteredDetectedObjects, bboxes_num),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "labels",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::ClusteredDetectedObjects, labels),  // bytes offset in struct
    nullptr,  // default value
    size_function__ClusteredDetectedObjects__labels,  // size() function pointer
    get_const_function__ClusteredDetectedObjects__labels,  // get_const(index) function pointer
    get_function__ClusteredDetectedObjects__labels,  // get(index) function pointer
    fetch_function__ClusteredDetectedObjects__labels,  // fetch(index, &value) function pointer
    assign_function__ClusteredDetectedObjects__labels,  // assign(index, value) function pointer
    resize_function__ClusteredDetectedObjects__labels  // resize(index) function pointer
  },
  {
    "scores",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::ClusteredDetectedObjects, scores),  // bytes offset in struct
    nullptr,  // default value
    size_function__ClusteredDetectedObjects__scores,  // size() function pointer
    get_const_function__ClusteredDetectedObjects__scores,  // get_const(index) function pointer
    get_function__ClusteredDetectedObjects__scores,  // get(index) function pointer
    fetch_function__ClusteredDetectedObjects__scores,  // fetch(index, &value) function pointer
    assign_function__ClusteredDetectedObjects__scores,  // assign(index, value) function pointer
    resize_function__ClusteredDetectedObjects__scores  // resize(index) function pointer
  },
  {
    "new_bbox_check",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::ClusteredDetectedObjects, new_bbox_check),  // bytes offset in struct
    nullptr,  // default value
    size_function__ClusteredDetectedObjects__new_bbox_check,  // size() function pointer
    get_const_function__ClusteredDetectedObjects__new_bbox_check,  // get_const(index) function pointer
    get_function__ClusteredDetectedObjects__new_bbox_check,  // get(index) function pointer
    fetch_function__ClusteredDetectedObjects__new_bbox_check,  // fetch(index, &value) function pointer
    assign_function__ClusteredDetectedObjects__new_bbox_check,  // assign(index, value) function pointer
    resize_function__ClusteredDetectedObjects__new_bbox_check  // resize(index) function pointer
  },
  {
    "id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::ClusteredDetectedObjects, id),  // bytes offset in struct
    nullptr,  // default value
    size_function__ClusteredDetectedObjects__id,  // size() function pointer
    get_const_function__ClusteredDetectedObjects__id,  // get_const(index) function pointer
    get_function__ClusteredDetectedObjects__id,  // get(index) function pointer
    fetch_function__ClusteredDetectedObjects__id,  // fetch(index, &value) function pointer
    assign_function__ClusteredDetectedObjects__id,  // assign(index, value) function pointer
    resize_function__ClusteredDetectedObjects__id  // resize(index) function pointer
  },
  {
    "pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<geometry_msgs::msg::Pose>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::ClusteredDetectedObjects, pose),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ClusteredDetectedObjects_message_members = {
  "det_msgs::msg",  // message namespace
  "ClusteredDetectedObjects",  // message name
  7,  // number of fields
  sizeof(det_msgs::msg::ClusteredDetectedObjects),
  ClusteredDetectedObjects_message_member_array,  // message members
  ClusteredDetectedObjects_init_function,  // function to initialize message memory (memory has to be allocated)
  ClusteredDetectedObjects_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ClusteredDetectedObjects_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ClusteredDetectedObjects_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace det_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<det_msgs::msg::ClusteredDetectedObjects>()
{
  return &::det_msgs::msg::rosidl_typesupport_introspection_cpp::ClusteredDetectedObjects_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, det_msgs, msg, ClusteredDetectedObjects)() {
  return &::det_msgs::msg::rosidl_typesupport_introspection_cpp::ClusteredDetectedObjects_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
