// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from det_msgs:msg/ClusteredDetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__STRUCT_HPP_
#define DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__det_msgs__msg__ClusteredDetectedObjects __attribute__((deprecated))
#else
# define DEPRECATED__det_msgs__msg__ClusteredDetectedObjects __declspec(deprecated)
#endif

namespace det_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ClusteredDetectedObjects_
{
  using Type = ClusteredDetectedObjects_<ContainerAllocator>;

  explicit ClusteredDetectedObjects_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->bboxes_num = 0ul;
    }
  }

  explicit ClusteredDetectedObjects_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->bboxes_num = 0ul;
    }
  }

  // field types and members
  using _bboxes_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _bboxes_type bboxes;
  using _bboxes_num_type =
    uint32_t;
  _bboxes_num_type bboxes_num;
  using _labels_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _labels_type labels;
  using _scores_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _scores_type scores;
  using _new_bbox_check_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _new_bbox_check_type new_bbox_check;
  using _id_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _id_type id;
  using _pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _pose_type pose;

  // setters for named parameter idiom
  Type & set__bboxes(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->bboxes = _arg;
    return *this;
  }
  Type & set__bboxes_num(
    const uint32_t & _arg)
  {
    this->bboxes_num = _arg;
    return *this;
  }
  Type & set__labels(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->labels = _arg;
    return *this;
  }
  Type & set__scores(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->scores = _arg;
    return *this;
  }
  Type & set__new_bbox_check(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->new_bbox_check = _arg;
    return *this;
  }
  Type & set__id(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator> *;
  using ConstRawPtr =
    const det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__det_msgs__msg__ClusteredDetectedObjects
    std::shared_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__det_msgs__msg__ClusteredDetectedObjects
    std::shared_ptr<det_msgs::msg::ClusteredDetectedObjects_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ClusteredDetectedObjects_ & other) const
  {
    if (this->bboxes != other.bboxes) {
      return false;
    }
    if (this->bboxes_num != other.bboxes_num) {
      return false;
    }
    if (this->labels != other.labels) {
      return false;
    }
    if (this->scores != other.scores) {
      return false;
    }
    if (this->new_bbox_check != other.new_bbox_check) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    if (this->pose != other.pose) {
      return false;
    }
    return true;
  }
  bool operator!=(const ClusteredDetectedObjects_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ClusteredDetectedObjects_

// alias to use template instance with default allocator
using ClusteredDetectedObjects =
  det_msgs::msg::ClusteredDetectedObjects_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace det_msgs

#endif  // DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__STRUCT_HPP_
