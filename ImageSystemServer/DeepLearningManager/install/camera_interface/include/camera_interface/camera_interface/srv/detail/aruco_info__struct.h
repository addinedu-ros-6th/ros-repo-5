// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from camera_interface:srv/ArucoInfo.idl
// generated code does not contain a copyright notice

#ifndef CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__STRUCT_H_
#define CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ArucoInfo in the package camera_interface.
typedef struct camera_interface__srv__ArucoInfo_Request
{
  bool aruco_info_req;
} camera_interface__srv__ArucoInfo_Request;

// Struct for a sequence of camera_interface__srv__ArucoInfo_Request.
typedef struct camera_interface__srv__ArucoInfo_Request__Sequence
{
  camera_interface__srv__ArucoInfo_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} camera_interface__srv__ArucoInfo_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ArucoInfo in the package camera_interface.
typedef struct camera_interface__srv__ArucoInfo_Response
{
  /// response
  int64_t aruco_id;
  double pos_x;
  double pos_y;
  double pos_z;
  double distance;
} camera_interface__srv__ArucoInfo_Response;

// Struct for a sequence of camera_interface__srv__ArucoInfo_Response.
typedef struct camera_interface__srv__ArucoInfo_Response__Sequence
{
  camera_interface__srv__ArucoInfo_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} camera_interface__srv__ArucoInfo_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CAMERA_INTERFACE__SRV__DETAIL__ARUCO_INFO__STRUCT_H_
