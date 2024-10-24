// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from det_msgs:msg/ClusteredDetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__TRAITS_HPP_
#define DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "det_msgs/msg/detail/clustered_detected_objects__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace det_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ClusteredDetectedObjects & msg,
  std::ostream & out)
{
  out << "{";
  // member: bboxes
  {
    if (msg.bboxes.size() == 0) {
      out << "bboxes: []";
    } else {
      out << "bboxes: [";
      size_t pending_items = msg.bboxes.size();
      for (auto item : msg.bboxes) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: bboxes_num
  {
    out << "bboxes_num: ";
    rosidl_generator_traits::value_to_yaml(msg.bboxes_num, out);
    out << ", ";
  }

  // member: labels
  {
    if (msg.labels.size() == 0) {
      out << "labels: []";
    } else {
      out << "labels: [";
      size_t pending_items = msg.labels.size();
      for (auto item : msg.labels) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: scores
  {
    if (msg.scores.size() == 0) {
      out << "scores: []";
    } else {
      out << "scores: [";
      size_t pending_items = msg.scores.size();
      for (auto item : msg.scores) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: new_bbox_check
  {
    if (msg.new_bbox_check.size() == 0) {
      out << "new_bbox_check: []";
    } else {
      out << "new_bbox_check: [";
      size_t pending_items = msg.new_bbox_check.size();
      for (auto item : msg.new_bbox_check) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: id
  {
    if (msg.id.size() == 0) {
      out << "id: []";
    } else {
      out << "id: [";
      size_t pending_items = msg.id.size();
      for (auto item : msg.id) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: pose
  {
    out << "pose: ";
    to_flow_style_yaml(msg.pose, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ClusteredDetectedObjects & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: bboxes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.bboxes.size() == 0) {
      out << "bboxes: []\n";
    } else {
      out << "bboxes:\n";
      for (auto item : msg.bboxes) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: bboxes_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "bboxes_num: ";
    rosidl_generator_traits::value_to_yaml(msg.bboxes_num, out);
    out << "\n";
  }

  // member: labels
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.labels.size() == 0) {
      out << "labels: []\n";
    } else {
      out << "labels:\n";
      for (auto item : msg.labels) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: scores
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.scores.size() == 0) {
      out << "scores: []\n";
    } else {
      out << "scores:\n";
      for (auto item : msg.scores) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: new_bbox_check
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.new_bbox_check.size() == 0) {
      out << "new_bbox_check: []\n";
    } else {
      out << "new_bbox_check:\n";
      for (auto item : msg.new_bbox_check) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.id.size() == 0) {
      out << "id: []\n";
    } else {
      out << "id:\n";
      for (auto item : msg.id) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pose:\n";
    to_block_style_yaml(msg.pose, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ClusteredDetectedObjects & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace det_msgs

namespace rosidl_generator_traits
{

[[deprecated("use det_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const det_msgs::msg::ClusteredDetectedObjects & msg,
  std::ostream & out, size_t indentation = 0)
{
  det_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use det_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const det_msgs::msg::ClusteredDetectedObjects & msg)
{
  return det_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<det_msgs::msg::ClusteredDetectedObjects>()
{
  return "det_msgs::msg::ClusteredDetectedObjects";
}

template<>
inline const char * name<det_msgs::msg::ClusteredDetectedObjects>()
{
  return "det_msgs/msg/ClusteredDetectedObjects";
}

template<>
struct has_fixed_size<det_msgs::msg::ClusteredDetectedObjects>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<det_msgs::msg::ClusteredDetectedObjects>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<det_msgs::msg::ClusteredDetectedObjects>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__TRAITS_HPP_
