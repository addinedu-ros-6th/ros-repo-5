// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from camera_interface:srv/ArucoInfo.idl
// generated code does not contain a copyright notice

#ifndef CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__BUILDER_HPP_
#define CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "camera_interface/srv/detail/aruco_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace camera_interface
{

namespace srv
{

namespace builder
{

class Init_ArucoInfo_Request_aruco_info_req
{
public:
  Init_ArucoInfo_Request_aruco_info_req()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::camera_interface::srv::ArucoInfo_Request aruco_info_req(::camera_interface::srv::ArucoInfo_Request::_aruco_info_req_type arg)
  {
    msg_.aruco_info_req = std::move(arg);
    return std::move(msg_);
  }

private:
  ::camera_interface::srv::ArucoInfo_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::camera_interface::srv::ArucoInfo_Request>()
{
  return camera_interface::srv::builder::Init_ArucoInfo_Request_aruco_info_req();
}

}  // namespace camera_interface


namespace camera_interface
{

namespace srv
{

namespace builder
{

class Init_ArucoInfo_Response_distance
{
public:
  explicit Init_ArucoInfo_Response_distance(::camera_interface::srv::ArucoInfo_Response & msg)
  : msg_(msg)
  {}
  ::camera_interface::srv::ArucoInfo_Response distance(::camera_interface::srv::ArucoInfo_Response::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::camera_interface::srv::ArucoInfo_Response msg_;
};

class Init_ArucoInfo_Response_pos_z
{
public:
  explicit Init_ArucoInfo_Response_pos_z(::camera_interface::srv::ArucoInfo_Response & msg)
  : msg_(msg)
  {}
  Init_ArucoInfo_Response_distance pos_z(::camera_interface::srv::ArucoInfo_Response::_pos_z_type arg)
  {
    msg_.pos_z = std::move(arg);
    return Init_ArucoInfo_Response_distance(msg_);
  }

private:
  ::camera_interface::srv::ArucoInfo_Response msg_;
};

class Init_ArucoInfo_Response_pos_y
{
public:
  explicit Init_ArucoInfo_Response_pos_y(::camera_interface::srv::ArucoInfo_Response & msg)
  : msg_(msg)
  {}
  Init_ArucoInfo_Response_pos_z pos_y(::camera_interface::srv::ArucoInfo_Response::_pos_y_type arg)
  {
    msg_.pos_y = std::move(arg);
    return Init_ArucoInfo_Response_pos_z(msg_);
  }

private:
  ::camera_interface::srv::ArucoInfo_Response msg_;
};

class Init_ArucoInfo_Response_pos_x
{
public:
  explicit Init_ArucoInfo_Response_pos_x(::camera_interface::srv::ArucoInfo_Response & msg)
  : msg_(msg)
  {}
  Init_ArucoInfo_Response_pos_y pos_x(::camera_interface::srv::ArucoInfo_Response::_pos_x_type arg)
  {
    msg_.pos_x = std::move(arg);
    return Init_ArucoInfo_Response_pos_y(msg_);
  }

private:
  ::camera_interface::srv::ArucoInfo_Response msg_;
};

class Init_ArucoInfo_Response_aruco_id
{
public:
  Init_ArucoInfo_Response_aruco_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ArucoInfo_Response_pos_x aruco_id(::camera_interface::srv::ArucoInfo_Response::_aruco_id_type arg)
  {
    msg_.aruco_id = std::move(arg);
    return Init_ArucoInfo_Response_pos_x(msg_);
  }

private:
  ::camera_interface::srv::ArucoInfo_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::camera_interface::srv::ArucoInfo_Response>()
{
  return camera_interface::srv::builder::Init_ArucoInfo_Response_aruco_id();
}

}  // namespace camera_interface

#endif  // CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__BUILDER_HPP_
