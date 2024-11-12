// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from taskmanager_msgs:srv/JobCompleteReq.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__SRV__DETAIL__JOB_COMPLETE_REQ__STRUCT_HPP_
#define TASKMANAGER_MSGS__SRV__DETAIL__JOB_COMPLETE_REQ__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Request __attribute__((deprecated))
#else
# define DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Request __declspec(deprecated)
#endif

namespace taskmanager_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct JobCompleteReq_Request_
{
  using Type = JobCompleteReq_Request_<ContainerAllocator>;

  explicit JobCompleteReq_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->job_id = 0ll;
      this->job_complete = 0ll;
      this->detected_sensor = 0ll;
    }
  }

  explicit JobCompleteReq_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->job_id = 0ll;
      this->job_complete = 0ll;
      this->detected_sensor = 0ll;
    }
  }

  // field types and members
  using _job_id_type =
    int64_t;
  _job_id_type job_id;
  using _job_complete_type =
    int64_t;
  _job_complete_type job_complete;
  using _detected_sensor_type =
    int64_t;
  _detected_sensor_type detected_sensor;

  // setters for named parameter idiom
  Type & set__job_id(
    const int64_t & _arg)
  {
    this->job_id = _arg;
    return *this;
  }
  Type & set__job_complete(
    const int64_t & _arg)
  {
    this->job_complete = _arg;
    return *this;
  }
  Type & set__detected_sensor(
    const int64_t & _arg)
  {
    this->detected_sensor = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Request
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Request
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const JobCompleteReq_Request_ & other) const
  {
    if (this->job_id != other.job_id) {
      return false;
    }
    if (this->job_complete != other.job_complete) {
      return false;
    }
    if (this->detected_sensor != other.detected_sensor) {
      return false;
    }
    return true;
  }
  bool operator!=(const JobCompleteReq_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct JobCompleteReq_Request_

// alias to use template instance with default allocator
using JobCompleteReq_Request =
  taskmanager_msgs::srv::JobCompleteReq_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace taskmanager_msgs


#ifndef _WIN32
# define DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Response __attribute__((deprecated))
#else
# define DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Response __declspec(deprecated)
#endif

namespace taskmanager_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct JobCompleteReq_Response_
{
  using Type = JobCompleteReq_Response_<ContainerAllocator>;

  explicit JobCompleteReq_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->receive_complete = 0ll;
    }
  }

  explicit JobCompleteReq_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->receive_complete = 0ll;
    }
  }

  // field types and members
  using _receive_complete_type =
    int64_t;
  _receive_complete_type receive_complete;

  // setters for named parameter idiom
  Type & set__receive_complete(
    const int64_t & _arg)
  {
    this->receive_complete = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Response
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__taskmanager_msgs__srv__JobCompleteReq_Response
    std::shared_ptr<taskmanager_msgs::srv::JobCompleteReq_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const JobCompleteReq_Response_ & other) const
  {
    if (this->receive_complete != other.receive_complete) {
      return false;
    }
    return true;
  }
  bool operator!=(const JobCompleteReq_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct JobCompleteReq_Response_

// alias to use template instance with default allocator
using JobCompleteReq_Response =
  taskmanager_msgs::srv::JobCompleteReq_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace taskmanager_msgs

namespace taskmanager_msgs
{

namespace srv
{

struct JobCompleteReq
{
  using Request = taskmanager_msgs::srv::JobCompleteReq_Request;
  using Response = taskmanager_msgs::srv::JobCompleteReq_Response;
};

}  // namespace srv

}  // namespace taskmanager_msgs

#endif  // TASKMANAGER_MSGS__SRV__DETAIL__JOB_COMPLETE_REQ__STRUCT_HPP_
