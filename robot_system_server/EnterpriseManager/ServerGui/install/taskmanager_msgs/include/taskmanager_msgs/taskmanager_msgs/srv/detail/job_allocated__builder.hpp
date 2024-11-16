// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from taskmanager_msgs:srv/JobAllocated.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__SRV__DETAIL__JOB_ALLOCATED__BUILDER_HPP_
#define TASKMANAGER_MSGS__SRV__DETAIL__JOB_ALLOCATED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "taskmanager_msgs/srv/detail/job_allocated__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace taskmanager_msgs
{

namespace srv
{

namespace builder
{

class Init_JobAllocated_Request_nav_id
{
public:
  explicit Init_JobAllocated_Request_nav_id(::taskmanager_msgs::srv::JobAllocated_Request & msg)
  : msg_(msg)
  {}
  ::taskmanager_msgs::srv::JobAllocated_Request nav_id(::taskmanager_msgs::srv::JobAllocated_Request::_nav_id_type arg)
  {
    msg_.nav_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Request msg_;
};

class Init_JobAllocated_Request_job_id
{
public:
  explicit Init_JobAllocated_Request_job_id(::taskmanager_msgs::srv::JobAllocated_Request & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_Request_nav_id job_id(::taskmanager_msgs::srv::JobAllocated_Request::_job_id_type arg)
  {
    msg_.job_id = std::move(arg);
    return Init_JobAllocated_Request_nav_id(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Request msg_;
};

class Init_JobAllocated_Request_w
{
public:
  explicit Init_JobAllocated_Request_w(::taskmanager_msgs::srv::JobAllocated_Request & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_Request_job_id w(::taskmanager_msgs::srv::JobAllocated_Request::_w_type arg)
  {
    msg_.w = std::move(arg);
    return Init_JobAllocated_Request_job_id(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Request msg_;
};

class Init_JobAllocated_Request_z
{
public:
  explicit Init_JobAllocated_Request_z(::taskmanager_msgs::srv::JobAllocated_Request & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_Request_w z(::taskmanager_msgs::srv::JobAllocated_Request::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_JobAllocated_Request_w(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Request msg_;
};

class Init_JobAllocated_Request_y
{
public:
  explicit Init_JobAllocated_Request_y(::taskmanager_msgs::srv::JobAllocated_Request & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_Request_z y(::taskmanager_msgs::srv::JobAllocated_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_JobAllocated_Request_z(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Request msg_;
};

class Init_JobAllocated_Request_x
{
public:
  explicit Init_JobAllocated_Request_x(::taskmanager_msgs::srv::JobAllocated_Request & msg)
  : msg_(msg)
  {}
  Init_JobAllocated_Request_y x(::taskmanager_msgs::srv::JobAllocated_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_JobAllocated_Request_y(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Request msg_;
};

class Init_JobAllocated_Request_robot_num
{
public:
  Init_JobAllocated_Request_robot_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_JobAllocated_Request_x robot_num(::taskmanager_msgs::srv::JobAllocated_Request::_robot_num_type arg)
  {
    msg_.robot_num = std::move(arg);
    return Init_JobAllocated_Request_x(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::taskmanager_msgs::srv::JobAllocated_Request>()
{
  return taskmanager_msgs::srv::builder::Init_JobAllocated_Request_robot_num();
}

}  // namespace taskmanager_msgs


namespace taskmanager_msgs
{

namespace srv
{

namespace builder
{

class Init_JobAllocated_Response_receive_complete
{
public:
  Init_JobAllocated_Response_receive_complete()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::taskmanager_msgs::srv::JobAllocated_Response receive_complete(::taskmanager_msgs::srv::JobAllocated_Response::_receive_complete_type arg)
  {
    msg_.receive_complete = std::move(arg);
    return std::move(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobAllocated_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::taskmanager_msgs::srv::JobAllocated_Response>()
{
  return taskmanager_msgs::srv::builder::Init_JobAllocated_Response_receive_complete();
}

}  // namespace taskmanager_msgs

#endif  // TASKMANAGER_MSGS__SRV__DETAIL__JOB_ALLOCATED__BUILDER_HPP_
