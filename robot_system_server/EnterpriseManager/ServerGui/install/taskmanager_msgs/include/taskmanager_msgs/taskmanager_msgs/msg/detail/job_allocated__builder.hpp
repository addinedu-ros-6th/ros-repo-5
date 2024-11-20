// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from taskmanager_msgs:msg/JobAllocated.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__BUILDER_HPP_
#define TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "taskmanager_msgs/msg/detail/job_allocated__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace taskmanager_msgs
{

namespace msg
{

namespace builder
{

class Init_JobAllocated_nav_id
{
public:
  explicit Init_JobAllocated_nav_id(::taskmanager_msgs::msg::JobAllocated & msg)
  : msg_(msg)
  {}
  ::taskmanager_msgs::msg::JobAllocated nav_id(::taskmanager_msgs::msg::JobAllocated::_nav_id_type arg)
  {
    msg_.nav_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::taskmanager_msgs::msg::JobAllocated msg_;
};

class Init_JobAllocated_job_id
{
public:
  explicit Init_JobAllocated_job_id(::taskmanager_msgs::msg::JobAllocated & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_nav_id job_id(::taskmanager_msgs::msg::JobAllocated::_job_id_type arg)
  {
    msg_.job_id = std::move(arg);
    return Init_JobAllocated_nav_id(msg_);
  }

private:
  ::taskmanager_msgs::msg::JobAllocated msg_;
};

class Init_JobAllocated_w
{
public:
  explicit Init_JobAllocated_w(::taskmanager_msgs::msg::JobAllocated & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_job_id w(::taskmanager_msgs::msg::JobAllocated::_w_type arg)
  {
    msg_.w = std::move(arg);
    return Init_JobAllocated_job_id(msg_);
  }

private:
  ::taskmanager_msgs::msg::JobAllocated msg_;
};

class Init_JobAllocated_z
{
public:
  explicit Init_JobAllocated_z(::taskmanager_msgs::msg::JobAllocated & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_w z(::taskmanager_msgs::msg::JobAllocated::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_JobAllocated_w(msg_);
  }

private:
  ::taskmanager_msgs::msg::JobAllocated msg_;
};

class Init_JobAllocated_y
{
public:
  explicit Init_JobAllocated_y(::taskmanager_msgs::msg::JobAllocated & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_z y(::taskmanager_msgs::msg::JobAllocated::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_JobAllocated_z(msg_);
  }

private:
  ::taskmanager_msgs::msg::JobAllocated msg_;
};

class Init_JobAllocated_x
{
public:
  explicit Init_JobAllocated_x(::taskmanager_msgs::msg::JobAllocated & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_y x(::taskmanager_msgs::msg::JobAllocated::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_JobAllocated_y(msg_);
  }

private:
  ::taskmanager_msgs::msg::JobAllocated msg_;
};

class Init_JobAllocated_robot_num
{
public:
  Init_JobAllocated_robot_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_JobAllocated_x robot_num(::taskmanager_msgs::msg::JobAllocated::_robot_num_type arg)
  {
    msg_.robot_num = std::move(arg);
    return Init_JobAllocated_x(msg_);
  }

private:
  ::taskmanager_msgs::msg::JobAllocated msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::taskmanager_msgs::msg::JobAllocated>()
{
  return taskmanager_msgs::msg::builder::Init_JobAllocated_robot_num();
}

}  // namespace taskmanager_msgs

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__BUILDER_HPP_
