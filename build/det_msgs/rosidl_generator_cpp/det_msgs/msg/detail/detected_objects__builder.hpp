// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from det_msgs:msg/DetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__BUILDER_HPP_
#define DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "det_msgs/msg/detail/detected_objects__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace det_msgs
{

namespace msg
{

namespace builder
{

class Init_DetectedObjects_scores
{
public:
  explicit Init_DetectedObjects_scores(::det_msgs::msg::DetectedObjects & msg)
  : msg_(msg)
  {}
  ::det_msgs::msg::DetectedObjects scores(::det_msgs::msg::DetectedObjects::_scores_type arg)
  {
    msg_.scores = std::move(arg);
    return std::move(msg_);
  }

private:
  ::det_msgs::msg::DetectedObjects msg_;
};

class Init_DetectedObjects_labels
{
public:
  explicit Init_DetectedObjects_labels(::det_msgs::msg::DetectedObjects & msg)
  : msg_(msg)
  {}
  Init_DetectedObjects_scores labels(::det_msgs::msg::DetectedObjects::_labels_type arg)
  {
    msg_.labels = std::move(arg);
    return Init_DetectedObjects_scores(msg_);
  }

private:
  ::det_msgs::msg::DetectedObjects msg_;
};

class Init_DetectedObjects_bboxes_num
{
public:
  explicit Init_DetectedObjects_bboxes_num(::det_msgs::msg::DetectedObjects & msg)
  : msg_(msg)
  {}
  Init_DetectedObjects_labels bboxes_num(::det_msgs::msg::DetectedObjects::_bboxes_num_type arg)
  {
    msg_.bboxes_num = std::move(arg);
    return Init_DetectedObjects_labels(msg_);
  }

private:
  ::det_msgs::msg::DetectedObjects msg_;
};

class Init_DetectedObjects_bboxes
{
public:
  Init_DetectedObjects_bboxes()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DetectedObjects_bboxes_num bboxes(::det_msgs::msg::DetectedObjects::_bboxes_type arg)
  {
    msg_.bboxes = std::move(arg);
    return Init_DetectedObjects_bboxes_num(msg_);
  }

private:
  ::det_msgs::msg::DetectedObjects msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::det_msgs::msg::DetectedObjects>()
{
  return det_msgs::msg::builder::Init_DetectedObjects_bboxes();
}

}  // namespace det_msgs

#endif  // DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__BUILDER_HPP_
