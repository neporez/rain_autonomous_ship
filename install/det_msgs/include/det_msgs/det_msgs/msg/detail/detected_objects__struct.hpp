// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from det_msgs:msg/DetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__STRUCT_HPP_
#define DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__det_msgs__msg__DetectedObjects __attribute__((deprecated))
#else
# define DEPRECATED__det_msgs__msg__DetectedObjects __declspec(deprecated)
#endif

namespace det_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DetectedObjects_
{
  using Type = DetectedObjects_<ContainerAllocator>;

  explicit DetectedObjects_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->bboxes_num = 0ul;
    }
  }

  explicit DetectedObjects_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
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

  // constant declarations

  // pointer types
  using RawPtr =
    det_msgs::msg::DetectedObjects_<ContainerAllocator> *;
  using ConstRawPtr =
    const det_msgs::msg::DetectedObjects_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      det_msgs::msg::DetectedObjects_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      det_msgs::msg::DetectedObjects_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__det_msgs__msg__DetectedObjects
    std::shared_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__det_msgs__msg__DetectedObjects
    std::shared_ptr<det_msgs::msg::DetectedObjects_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DetectedObjects_ & other) const
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
    return true;
  }
  bool operator!=(const DetectedObjects_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DetectedObjects_

// alias to use template instance with default allocator
using DetectedObjects =
  det_msgs::msg::DetectedObjects_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace det_msgs

#endif  // DET_MSGS__MSG__DETAIL__DETECTED_OBJECTS__STRUCT_HPP_
