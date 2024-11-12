// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from taskmanager_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__TRAITS_HPP_
#define TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "taskmanager_msgs/msg/detail/robot_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace taskmanager_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RobotStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_status
  {
    out << "robot_status: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_status, out);
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

  // member: battery_status
  {
    out << "battery_status: ";
    rosidl_generator_traits::value_to_yaml(msg.battery_status, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_status: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_status, out);
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

  // member: battery_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "battery_status: ";
    rosidl_generator_traits::value_to_yaml(msg.battery_status, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotStatus & msg, bool use_flow_style = false)
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
  const taskmanager_msgs::msg::RobotStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  taskmanager_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use taskmanager_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const taskmanager_msgs::msg::RobotStatus & msg)
{
  return taskmanager_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<taskmanager_msgs::msg::RobotStatus>()
{
  return "taskmanager_msgs::msg::RobotStatus";
}

template<>
inline const char * name<taskmanager_msgs::msg::RobotStatus>()
{
  return "taskmanager_msgs/msg/RobotStatus";
}

template<>
struct has_fixed_size<taskmanager_msgs::msg::RobotStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<taskmanager_msgs::msg::RobotStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<taskmanager_msgs::msg::RobotStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__TRAITS_HPP_
