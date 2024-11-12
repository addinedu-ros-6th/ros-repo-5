// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from taskmanager_msgs:srv/JobCompleteReq.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__SRV__DETAIL__JOB_COMPLETE_REQ__BUILDER_HPP_
#define TASKMANAGER_MSGS__SRV__DETAIL__JOB_COMPLETE_REQ__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "taskmanager_msgs/srv/detail/job_complete_req__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace taskmanager_msgs
{

namespace srv
{

namespace builder
{

class Init_JobCompleteReq_Request_detected_sensor
{
public:
  explicit Init_JobCompleteReq_Request_detected_sensor(::taskmanager_msgs::srv::JobCompleteReq_Request & msg)
  : msg_(msg)
  {}
  ::taskmanager_msgs::srv::JobCompleteReq_Request detected_sensor(::taskmanager_msgs::srv::JobCompleteReq_Request::_detected_sensor_type arg)
  {
    msg_.detected_sensor = std::move(arg);
    return std::move(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobCompleteReq_Request msg_;
};

class Init_JobCompleteReq_Request_job_complete
{
public:
  explicit Init_JobCompleteReq_Request_job_complete(::taskmanager_msgs::srv::JobCompleteReq_Request & msg)
  : msg_(msg)
  {}
  Init_JobCompleteReq_Request_detected_sensor job_complete(::taskmanager_msgs::srv::JobCompleteReq_Request::_job_complete_type arg)
  {
    msg_.job_complete = std::move(arg);
    return Init_JobCompleteReq_Request_detected_sensor(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobCompleteReq_Request msg_;
};

class Init_JobCompleteReq_Request_job_id
{
public:
  Init_JobCompleteReq_Request_job_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_JobCompleteReq_Request_job_complete job_id(::taskmanager_msgs::srv::JobCompleteReq_Request::_job_id_type arg)
  {
    msg_.job_id = std::move(arg);
    return Init_JobCompleteReq_Request_job_complete(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobCompleteReq_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::taskmanager_msgs::srv::JobCompleteReq_Request>()
{
  return taskmanager_msgs::srv::builder::Init_JobCompleteReq_Request_job_id();
}

}  // namespace taskmanager_msgs


namespace taskmanager_msgs
{

namespace srv
{

namespace builder
{

class Init_JobCompleteReq_Response_receive_complete
{
public:
  Init_JobCompleteReq_Response_receive_complete()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::taskmanager_msgs::srv::JobCompleteReq_Response receive_complete(::taskmanager_msgs::srv::JobCompleteReq_Response::_receive_complete_type arg)
  {
    msg_.receive_complete = std::move(arg);
    return std::move(msg_);
  }

private:
  ::taskmanager_msgs::srv::JobCompleteReq_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::taskmanager_msgs::srv::JobCompleteReq_Response>()
{
  return taskmanager_msgs::srv::builder::Init_JobCompleteReq_Response_receive_complete();
}

}  // namespace taskmanager_msgs

#endif  // TASKMANAGER_MSGS__SRV__DETAIL__JOB_COMPLETE_REQ__BUILDER_HPP_
