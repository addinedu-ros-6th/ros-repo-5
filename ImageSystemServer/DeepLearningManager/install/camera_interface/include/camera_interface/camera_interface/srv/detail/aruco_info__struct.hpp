// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from camera_interface:srv/ArucoInfo.idl
// generated code does not contain a copyright notice

#ifndef CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__STRUCT_HPP_
#define CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__camera_interface__srv__ArucoInfo_Request __attribute__((deprecated))
#else
# define DEPRECATED__camera_interface__srv__ArucoInfo_Request __declspec(deprecated)
#endif

namespace camera_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ArucoInfo_Request_
{
  using Type = ArucoInfo_Request_<ContainerAllocator>;

  explicit ArucoInfo_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->aruco_info_req = false;
    }
  }

  explicit ArucoInfo_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->aruco_info_req = false;
    }
  }

  // field types and members
  using _aruco_info_req_type =
    bool;
  _aruco_info_req_type aruco_info_req;

  // setters for named parameter idiom
  Type & set__aruco_info_req(
    const bool & _arg)
  {
    this->aruco_info_req = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    camera_interface::srv::ArucoInfo_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const camera_interface::srv::ArucoInfo_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      camera_interface::srv::ArucoInfo_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      camera_interface::srv::ArucoInfo_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__camera_interface__srv__ArucoInfo_Request
    std::shared_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__camera_interface__srv__ArucoInfo_Request
    std::shared_ptr<camera_interface::srv::ArucoInfo_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ArucoInfo_Request_ & other) const
  {
    if (this->aruco_info_req != other.aruco_info_req) {
      return false;
    }
    return true;
  }
  bool operator!=(const ArucoInfo_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ArucoInfo_Request_

// alias to use template instance with default allocator
using ArucoInfo_Request =
  camera_interface::srv::ArucoInfo_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace camera_interface


#ifndef _WIN32
# define DEPRECATED__camera_interface__srv__ArucoInfo_Response __attribute__((deprecated))
#else
# define DEPRECATED__camera_interface__srv__ArucoInfo_Response __declspec(deprecated)
#endif

namespace camera_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ArucoInfo_Response_
{
  using Type = ArucoInfo_Response_<ContainerAllocator>;

  explicit ArucoInfo_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->aruco_id = 0ll;
      this->pos_x = 0.0;
      this->pos_y = 0.0;
      this->pos_z = 0.0;
      this->distance = 0.0;
    }
  }

  explicit ArucoInfo_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->aruco_id = 0ll;
      this->pos_x = 0.0;
      this->pos_y = 0.0;
      this->pos_z = 0.0;
      this->distance = 0.0;
    }
  }

  // field types and members
  using _aruco_id_type =
    int64_t;
  _aruco_id_type aruco_id;
  using _pos_x_type =
    double;
  _pos_x_type pos_x;
  using _pos_y_type =
    double;
  _pos_y_type pos_y;
  using _pos_z_type =
    double;
  _pos_z_type pos_z;
  using _distance_type =
    double;
  _distance_type distance;

  // setters for named parameter idiom
  Type & set__aruco_id(
    const int64_t & _arg)
  {
    this->aruco_id = _arg;
    return *this;
  }
  Type & set__pos_x(
    const double & _arg)
  {
    this->pos_x = _arg;
    return *this;
  }
  Type & set__pos_y(
    const double & _arg)
  {
    this->pos_y = _arg;
    return *this;
  }
  Type & set__pos_z(
    const double & _arg)
  {
    this->pos_z = _arg;
    return *this;
  }
  Type & set__distance(
    const double & _arg)
  {
    this->distance = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    camera_interface::srv::ArucoInfo_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const camera_interface::srv::ArucoInfo_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      camera_interface::srv::ArucoInfo_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      camera_interface::srv::ArucoInfo_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__camera_interface__srv__ArucoInfo_Response
    std::shared_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__camera_interface__srv__ArucoInfo_Response
    std::shared_ptr<camera_interface::srv::ArucoInfo_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ArucoInfo_Response_ & other) const
  {
    if (this->aruco_id != other.aruco_id) {
      return false;
    }
    if (this->pos_x != other.pos_x) {
      return false;
    }
    if (this->pos_y != other.pos_y) {
      return false;
    }
    if (this->pos_z != other.pos_z) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    return true;
  }
  bool operator!=(const ArucoInfo_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ArucoInfo_Response_

// alias to use template instance with default allocator
using ArucoInfo_Response =
  camera_interface::srv::ArucoInfo_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace camera_interface

namespace camera_interface
{

namespace srv
{

struct ArucoInfo
{
  using Request = camera_interface::srv::ArucoInfo_Request;
  using Response = camera_interface::srv::ArucoInfo_Response;
};

}  // namespace srv

}  // namespace camera_interface

#endif  // CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__STRUCT_HPP_
