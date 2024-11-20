// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from taskmanager_msgs:msg/JobAllocated.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__STRUCT_HPP_
#define TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__taskmanager_msgs__msg__JobAllocated __attribute__((deprecated))
#else
# define DEPRECATED__taskmanager_msgs__msg__JobAllocated __declspec(deprecated)
#endif

namespace taskmanager_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct JobAllocated_
{
  using Type = JobAllocated_<ContainerAllocator>;

  explicit JobAllocated_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_num = 0ll;
      this->x = 0.0;
      this->y = 0.0;
      this->z = 0.0;
      this->w = 0.0;
      this->job_id = 0ll;
      this->nav_id = 0ll;
    }
  }

  explicit JobAllocated_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_num = 0ll;
      this->x = 0.0;
      this->y = 0.0;
      this->z = 0.0;
      this->w = 0.0;
      this->job_id = 0ll;
      this->nav_id = 0ll;
    }
  }

  // field types and members
  using _robot_num_type =
    int64_t;
  _robot_num_type robot_num;
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    double;
  _y_type y;
  using _z_type =
    double;
  _z_type z;
  using _w_type =
    double;
  _w_type w;
  using _job_id_type =
    int64_t;
  _job_id_type job_id;
  using _nav_id_type =
    int64_t;
  _nav_id_type nav_id;

  // setters for named parameter idiom
  Type & set__robot_num(
    const int64_t & _arg)
  {
    this->robot_num = _arg;
    return *this;
  }
  Type & set__x(
    const double & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const double & _arg)
  {
    this->z = _arg;
    return *this;
  }
  Type & set__w(
    const double & _arg)
  {
    this->w = _arg;
    return *this;
  }
  Type & set__job_id(
    const int64_t & _arg)
  {
    this->job_id = _arg;
    return *this;
  }
  Type & set__nav_id(
    const int64_t & _arg)
  {
    this->nav_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    taskmanager_msgs::msg::JobAllocated_<ContainerAllocator> *;
  using ConstRawPtr =
    const taskmanager_msgs::msg::JobAllocated_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      taskmanager_msgs::msg::JobAllocated_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      taskmanager_msgs::msg::JobAllocated_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__taskmanager_msgs__msg__JobAllocated
    std::shared_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__taskmanager_msgs__msg__JobAllocated
    std::shared_ptr<taskmanager_msgs::msg::JobAllocated_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const JobAllocated_ & other) const
  {
    if (this->robot_num != other.robot_num) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    if (this->w != other.w) {
      return false;
    }
    if (this->job_id != other.job_id) {
      return false;
    }
    if (this->nav_id != other.nav_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const JobAllocated_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct JobAllocated_

// alias to use template instance with default allocator
using JobAllocated =
  taskmanager_msgs::msg::JobAllocated_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace taskmanager_msgs

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__STRUCT_HPP_