// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from det_msgs:msg/DetectedObjects.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "det_msgs/msg/detail/detected_objects__struct.hpp"
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

void DetectedObjects_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) det_msgs::msg::DetectedObjects(_init);
}

void DetectedObjects_fini_function(void * message_memory)
{
  auto typed_message = static_cast<det_msgs::msg::DetectedObjects *>(message_memory);
  typed_message->~DetectedObjects();
}

size_t size_function__DetectedObjects__bboxes(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectedObjects__bboxes(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectedObjects__bboxes(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectedObjects__bboxes(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__DetectedObjects__bboxes(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__DetectedObjects__bboxes(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__DetectedObjects__bboxes(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__DetectedObjects__bboxes(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__DetectedObjects__labels(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectedObjects__labels(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectedObjects__labels(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectedObjects__labels(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__DetectedObjects__labels(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__DetectedObjects__labels(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__DetectedObjects__labels(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__DetectedObjects__labels(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__DetectedObjects__scores(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectedObjects__scores(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectedObjects__scores(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectedObjects__scores(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__DetectedObjects__scores(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__DetectedObjects__scores(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__DetectedObjects__scores(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__DetectedObjects__scores(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember DetectedObjects_message_member_array[4] = {
  {
    "bboxes",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::DetectedObjects, bboxes),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectedObjects__bboxes,  // size() function pointer
    get_const_function__DetectedObjects__bboxes,  // get_const(index) function pointer
    get_function__DetectedObjects__bboxes,  // get(index) function pointer
    fetch_function__DetectedObjects__bboxes,  // fetch(index, &value) function pointer
    assign_function__DetectedObjects__bboxes,  // assign(index, value) function pointer
    resize_function__DetectedObjects__bboxes  // resize(index) function pointer
  },
  {
    "bboxes_num",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::DetectedObjects, bboxes_num),  // bytes offset in struct
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
    offsetof(det_msgs::msg::DetectedObjects, labels),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectedObjects__labels,  // size() function pointer
    get_const_function__DetectedObjects__labels,  // get_const(index) function pointer
    get_function__DetectedObjects__labels,  // get(index) function pointer
    fetch_function__DetectedObjects__labels,  // fetch(index, &value) function pointer
    assign_function__DetectedObjects__labels,  // assign(index, value) function pointer
    resize_function__DetectedObjects__labels  // resize(index) function pointer
  },
  {
    "scores",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(det_msgs::msg::DetectedObjects, scores),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectedObjects__scores,  // size() function pointer
    get_const_function__DetectedObjects__scores,  // get_const(index) function pointer
    get_function__DetectedObjects__scores,  // get(index) function pointer
    fetch_function__DetectedObjects__scores,  // fetch(index, &value) function pointer
    assign_function__DetectedObjects__scores,  // assign(index, value) function pointer
    resize_function__DetectedObjects__scores  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers DetectedObjects_message_members = {
  "det_msgs::msg",  // message namespace
  "DetectedObjects",  // message name
  4,  // number of fields
  sizeof(det_msgs::msg::DetectedObjects),
  DetectedObjects_message_member_array,  // message members
  DetectedObjects_init_function,  // function to initialize message memory (memory has to be allocated)
  DetectedObjects_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t DetectedObjects_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &DetectedObjects_message_members,
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
get_message_type_support_handle<det_msgs::msg::DetectedObjects>()
{
  return &::det_msgs::msg::rosidl_typesupport_introspection_cpp::DetectedObjects_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, det_msgs, msg, DetectedObjects)() {
  return &::det_msgs::msg::rosidl_typesupport_introspection_cpp::DetectedObjects_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
