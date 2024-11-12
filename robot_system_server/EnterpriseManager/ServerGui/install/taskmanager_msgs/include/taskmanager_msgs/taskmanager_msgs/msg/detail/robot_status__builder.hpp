// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from taskmanager_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_
#define TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "taskmanager_msgs/msg/detail/robot_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace taskmanager_msgs
{

namespace msg
{

namespace builder
{

class Init_RobotStatus_battery_status
{
public:
  explicit Init_RobotStatus_battery_status(::taskmanager_msgs::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  ::taskmanager_msgs::msg::RobotStatus battery_status(::taskmanager_msgs::msg::RobotStatus::_battery_status_type arg)
  {
    msg_.battery_status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::taskmanager_msgs::msg::RobotStatus msg_;
};

class Init_RobotStatus_y
{
public:
  explicit Init_RobotStatus_y(::taskmanager_msgs::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_battery_status y(::taskmanager_msgs::msg::RobotStatus::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_RobotStatus_battery_status(msg_);
  }

private:
  ::taskmanager_msgs::msg::RobotStatus msg_;
};

class Init_RobotStatus_x
{
public:
  explicit Init_RobotStatus_x(::taskmanager_msgs::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_y x(::taskmanager_msgs::msg::RobotStatus::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_RobotStatus_y(msg_);
  }

private:
  ::taskmanager_msgs::msg::RobotStatus msg_;
};

class Init_RobotStatus_robot_status
{
public:
  Init_RobotStatus_robot_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotStatus_x robot_status(::taskmanager_msgs::msg::RobotStatus::_robot_status_type arg)
  {
    msg_.robot_status = std::move(arg);
    return Init_RobotStatus_x(msg_);
  }

private:
  ::taskmanager_msgs::msg::RobotStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::taskmanager_msgs::msg::RobotStatus>()
{
  return taskmanager_msgs::msg::builder::Init_RobotStatus_robot_status();
}

}  // namespace taskmanager_msgs

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_
