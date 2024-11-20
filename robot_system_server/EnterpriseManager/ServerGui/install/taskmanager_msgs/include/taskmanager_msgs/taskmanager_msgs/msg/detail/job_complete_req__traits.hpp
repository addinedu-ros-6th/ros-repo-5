// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from taskmanager_msgs:msg/JobCompleteReq.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__JOB_COMPLETE_REQ__TRAITS_HPP_
#define TASKMANAGER_MSGS__MSG__DETAIL__JOB_COMPLETE_REQ__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "taskmanager_msgs/msg/detail/job_complete_req__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace taskmanager_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const JobCompleteReq & msg,
  std::ostream & out)
{
  out << "{";
  // member: job_id
  {
    out << "job_id: ";
    rosidl_generator_traits::value_to_yaml(msg.job_id, out);
    out << ", ";
  }

  // member: job_complete
  {
    out << "job_complete: ";
    rosidl_generator_traits::value_to_yaml(msg.job_complete, out);
    out << ", ";
  }

  // member: detected_sensor
  {
    out << "detected_sensor: ";
    rosidl_generator_traits::value_to_yaml(msg.detected_sensor, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const JobCompleteReq & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: job_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "job_id: ";
    rosidl_generator_traits::value_to_yaml(msg.job_id, out);
    out << "\n";
  }

  // member: job_complete
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "job_complete: ";
    rosidl_generator_traits::value_to_yaml(msg.job_complete, out);
    out << "\n";
  }

  // member: detected_sensor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "detected_sensor: ";
    rosidl_generator_traits::value_to_yaml(msg.detected_sensor, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const JobCompleteReq & msg, bool use_flow_style = false)
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
  const taskmanager_msgs::msg::JobCompleteReq & msg,
  std::ostream & out, size_t indentation = 0)
{
  taskmanager_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use taskmanager_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const taskmanager_msgs::msg::JobCompleteReq & msg)
{
  return taskmanager_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<taskmanager_msgs::msg::JobCompleteReq>()
{
  return "taskmanager_msgs::msg::JobCompleteReq";
}

template<>
inline const char * name<taskmanager_msgs::msg::JobCompleteReq>()
{
  return "taskmanager_msgs/msg/JobCompleteReq";
}

template<>
struct has_fixed_size<taskmanager_msgs::msg::JobCompleteReq>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<taskmanager_msgs::msg::JobCompleteReq>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<taskmanager_msgs::msg::JobCompleteReq>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__JOB_COMPLETE_REQ__TRAITS_HPP_
