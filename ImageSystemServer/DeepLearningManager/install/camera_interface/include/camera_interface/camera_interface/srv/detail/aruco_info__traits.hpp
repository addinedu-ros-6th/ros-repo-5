// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from camera_interface:srv/ArucoInfo.idl
// generated code does not contain a copyright notice

#ifndef CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__TRAITS_HPP_
#define CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "camera_interface/srv/detail/aruco_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace camera_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const ArucoInfo_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: aruco_info_req
  {
    out << "aruco_info_req: ";
    rosidl_generator_traits::value_to_yaml(msg.aruco_info_req, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ArucoInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: aruco_info_req
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "aruco_info_req: ";
    rosidl_generator_traits::value_to_yaml(msg.aruco_info_req, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ArucoInfo_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace camera_interface

namespace rosidl_generator_traits
{

[[deprecated("use camera_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const camera_interface::srv::ArucoInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  camera_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use camera_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const camera_interface::srv::ArucoInfo_Request & msg)
{
  return camera_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<camera_interface::srv::ArucoInfo_Request>()
{
  return "camera_interface::srv::ArucoInfo_Request";
}

template<>
inline const char * name<camera_interface::srv::ArucoInfo_Request>()
{
  return "camera_interface/srv/ArucoInfo_Request";
}

template<>
struct has_fixed_size<camera_interface::srv::ArucoInfo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<camera_interface::srv::ArucoInfo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<camera_interface::srv::ArucoInfo_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace camera_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const ArucoInfo_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: aruco_id
  {
    out << "aruco_id: ";
    rosidl_generator_traits::value_to_yaml(msg.aruco_id, out);
    out << ", ";
  }

  // member: pos_x
  {
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << ", ";
  }

  // member: pos_y
  {
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
    out << ", ";
  }

  // member: pos_z
  {
    out << "pos_z: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_z, out);
    out << ", ";
  }

  // member: distance
  {
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ArucoInfo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: aruco_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "aruco_id: ";
    rosidl_generator_traits::value_to_yaml(msg.aruco_id, out);
    out << "\n";
  }

  // member: pos_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << "\n";
  }

  // member: pos_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
    out << "\n";
  }

  // member: pos_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_z: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_z, out);
    out << "\n";
  }

  // member: distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ArucoInfo_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace camera_interface

namespace rosidl_generator_traits
{

[[deprecated("use camera_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const camera_interface::srv::ArucoInfo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  camera_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use camera_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const camera_interface::srv::ArucoInfo_Response & msg)
{
  return camera_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<camera_interface::srv::ArucoInfo_Response>()
{
  return "camera_interface::srv::ArucoInfo_Response";
}

template<>
inline const char * name<camera_interface::srv::ArucoInfo_Response>()
{
  return "camera_interface/srv/ArucoInfo_Response";
}

template<>
struct has_fixed_size<camera_interface::srv::ArucoInfo_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<camera_interface::srv::ArucoInfo_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<camera_interface::srv::ArucoInfo_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<camera_interface::srv::ArucoInfo>()
{
  return "camera_interface::srv::ArucoInfo";
}

template<>
inline const char * name<camera_interface::srv::ArucoInfo>()
{
  return "camera_interface/srv/ArucoInfo";
}

template<>
struct has_fixed_size<camera_interface::srv::ArucoInfo>
  : std::integral_constant<
    bool,
    has_fixed_size<camera_interface::srv::ArucoInfo_Request>::value &&
    has_fixed_size<camera_interface::srv::ArucoInfo_Response>::value
  >
{
};

template<>
struct has_bounded_size<camera_interface::srv::ArucoInfo>
  : std::integral_constant<
    bool,
    has_bounded_size<camera_interface::srv::ArucoInfo_Request>::value &&
    has_bounded_size<camera_interface::srv::ArucoInfo_Response>::value
  >
{
};

template<>
struct is_service<camera_interface::srv::ArucoInfo>
  : std::true_type
{
};

template<>
struct is_service_request<camera_interface::srv::ArucoInfo_Request>
  : std::true_type
{
};

template<>
struct is_service_response<camera_interface::srv::ArucoInfo_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__TRAITS_HPP_
