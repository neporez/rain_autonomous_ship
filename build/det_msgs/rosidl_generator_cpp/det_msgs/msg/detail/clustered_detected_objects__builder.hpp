// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from det_msgs:msg/ClusteredDetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__BUILDER_HPP_
#define DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "det_msgs/msg/detail/clustered_detected_objects__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace det_msgs
{

namespace msg
{

namespace builder
{

class Init_ClusteredDetectedObjects_pose
{
public:
  explicit Init_ClusteredDetectedObjects_pose(::det_msgs::msg::ClusteredDetectedObjects & msg)
  : msg_(msg)
  {}
  ::det_msgs::msg::ClusteredDetectedObjects pose(::det_msgs::msg::ClusteredDetectedObjects::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::det_msgs::msg::ClusteredDetectedObjects msg_;
};

class Init_ClusteredDetectedObjects_id
{
public:
  explicit Init_ClusteredDetectedObjects_id(::det_msgs::msg::ClusteredDetectedObjects & msg)
  : msg_(msg)
  {}
  Init_ClusteredDetectedObjects_pose id(::det_msgs::msg::ClusteredDetectedObjects::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_ClusteredDetectedObjects_pose(msg_);
  }

private:
  ::det_msgs::msg::ClusteredDetectedObjects msg_;
};

class Init_ClusteredDetectedObjects_new_bbox_check
{
public:
  explicit Init_ClusteredDetectedObjects_new_bbox_check(::det_msgs::msg::ClusteredDetectedObjects & msg)
  : msg_(msg)
  {}
  Init_ClusteredDetectedObjects_id new_bbox_check(::det_msgs::msg::ClusteredDetectedObjects::_new_bbox_check_type arg)
  {
    msg_.new_bbox_check = std::move(arg);
    return Init_ClusteredDetectedObjects_id(msg_);
  }

private:
  ::det_msgs::msg::ClusteredDetectedObjects msg_;
};

class Init_ClusteredDetectedObjects_scores
{
public:
  explicit Init_ClusteredDetectedObjects_scores(::det_msgs::msg::ClusteredDetectedObjects & msg)
  : msg_(msg)
  {}
  Init_ClusteredDetectedObjects_new_bbox_check scores(::det_msgs::msg::ClusteredDetectedObjects::_scores_type arg)
  {
    msg_.scores = std::move(arg);
    return Init_ClusteredDetectedObjects_new_bbox_check(msg_);
  }

private:
  ::det_msgs::msg::ClusteredDetectedObjects msg_;
};

class Init_ClusteredDetectedObjects_labels
{
public:
  explicit Init_ClusteredDetectedObjects_labels(::det_msgs::msg::ClusteredDetectedObjects & msg)
  : msg_(msg)
  {}
  Init_ClusteredDetectedObjects_scores labels(::det_msgs::msg::ClusteredDetectedObjects::_labels_type arg)
  {
    msg_.labels = std::move(arg);
    return Init_ClusteredDetectedObjects_scores(msg_);
  }

private:
  ::det_msgs::msg::ClusteredDetectedObjects msg_;
};

class Init_ClusteredDetectedObjects_bboxes_num
{
public:
  explicit Init_ClusteredDetectedObjects_bboxes_num(::det_msgs::msg::ClusteredDetectedObjects & msg)
  : msg_(msg)
  {}
  Init_ClusteredDetectedObjects_labels bboxes_num(::det_msgs::msg::ClusteredDetectedObjects::_bboxes_num_type arg)
  {
    msg_.bboxes_num = std::move(arg);
    return Init_ClusteredDetectedObjects_labels(msg_);
  }

private:
  ::det_msgs::msg::ClusteredDetectedObjects msg_;
};

class Init_ClusteredDetectedObjects_bboxes
{
public:
  Init_ClusteredDetectedObjects_bboxes()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ClusteredDetectedObjects_bboxes_num bboxes(::det_msgs::msg::ClusteredDetectedObjects::_bboxes_type arg)
  {
    msg_.bboxes = std::move(arg);
    return Init_ClusteredDetectedObjects_bboxes_num(msg_);
  }

private:
  ::det_msgs::msg::ClusteredDetectedObjects msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::det_msgs::msg::ClusteredDetectedObjects>()
{
  return det_msgs::msg::builder::Init_ClusteredDetectedObjects_bboxes();
}

}  // namespace det_msgs

#endif  // DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__BUILDER_HPP_
