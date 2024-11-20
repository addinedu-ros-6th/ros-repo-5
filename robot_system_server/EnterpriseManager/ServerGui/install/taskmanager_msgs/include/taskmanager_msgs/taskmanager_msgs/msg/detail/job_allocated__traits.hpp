// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from taskmanager_msgs:msg/JobAllocated.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__TRAITS_HPP_
#define TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "taskmanager_msgs/msg/detail/job_allocated__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace taskmanager_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const JobAllocated & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_num
  {
    out << "robot_num: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_num, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: z
  {
    out << "z: ";
    rosidl_generator_traits::value_to_yaml(msg.z, out);
    out << ", ";
  }

  // member: w
  {
    out << "w: ";
    rosidl_generator_traits::value_to_yaml(msg.w, out);
    out << ", ";
  }

  // member: job_id
  {
    out << "job_id: ";
    rosidl_generator_traits::value_to_yaml(msg.job_id, out);
    out << ", ";
  }

  // member: nav_id
  {
    out << "nav_id: ";
    rosidl_generator_traits::value_to_yaml(msg.nav_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const JobAllocated & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_num: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_num, out);
    out << "\n";
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "z: ";
    rosidl_generator_traits::value_to_yaml(msg.z, out);
    out << "\n";
  }

  // member: w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "w: ";
    rosidl_generator_traits::value_to_yaml(msg.w, out);
    out << "\n";
  }

  // member: job_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "job_id: ";
    rosidl_generator_traits::value_to_yaml(msg.job_id, out);
    out << "\n";
  }

  // member: nav_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "nav_id: ";
    rosidl_generator_traits::value_to_yaml(msg.nav_id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const JobAllocated & msg, bool use_flow_style = false)
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

}  // namespace taskmanager_msgs

namespace rosidl_generator_traits
{

[[deprecated("use taskmanager_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const taskmanager_msgs::msg::JobAllocated & msg,
  std::ostream & out, size_t indentation = 0)
{
  taskmanager_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use taskmanager_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const taskmanager_msgs::msg::JobAllocated & msg)
{
  return taskmanager_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<taskmanager_msgs::msg::JobAllocated>()
{
  return "taskmanager_msgs::msg::JobAllocated";
}

template<>
inline const char * name<taskmanager_msgs::msg::JobAllocated>()
{
  return "taskmanager_msgs/msg/JobAllocated";
}

template<>
struct has_fixed_size<taskmanager_msgs::msg::JobAllocated>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<taskmanager_msgs::msg::JobAllocated>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<taskmanager_msgs::msg::JobAllocated>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__TRAITS_HPP_
