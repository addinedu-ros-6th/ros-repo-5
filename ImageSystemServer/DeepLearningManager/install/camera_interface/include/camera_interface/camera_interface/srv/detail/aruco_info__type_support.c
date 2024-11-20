// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from camera_interface:srv/ArucoInfo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "camera_interface/srv/detail/aruco_info__rosidl_typesupport_introspection_c.h"
#include "camera_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "camera_interface/srv/detail/aruco_info__functions.h"
#include "camera_interface/srv/detail/aruco_info__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  camera_interface__srv__ArucoInfo_Request__init(message_memory);
}

void camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_fini_function(void * message_memory)
{
  camera_interface__srv__ArucoInfo_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_member_array[1] = {
  {
    "aruco_info_req",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(camera_interface__srv__ArucoInfo_Request, aruco_info_req),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_members = {
  "camera_interface__srv",  // message namespace
  "ArucoInfo_Request",  // message name
  1,  // number of fields
  sizeof(camera_interface__srv__ArucoInfo_Request),
  camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_member_array,  // message members
  camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_type_support_handle = {
  0,
  &camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_camera_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, camera_interface, srv, ArucoInfo_Request)() {
  if (!camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_type_support_handle.typesupport_identifier) {
    camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &camera_interface__srv__ArucoInfo_Request__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "camera_interface/srv/detail/aruco_info__rosidl_typesupport_introspection_c.h"
// already included above
// #include "camera_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "camera_interface/srv/detail/aruco_info__functions.h"
// already included above
// #include "camera_interface/srv/detail/aruco_info__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  camera_interface__srv__ArucoInfo_Response__init(message_memory);
}

void camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_fini_function(void * message_memory)
{
  camera_interface__srv__ArucoInfo_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_member_array[5] = {
  {
    "aruco_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(camera_interface__srv__ArucoInfo_Response, aruco_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(camera_interface__srv__ArucoInfo_Response, pos_x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(camera_interface__srv__ArucoInfo_Response, pos_y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos_z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(camera_interface__srv__ArucoInfo_Response, pos_z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "distance",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(camera_interface__srv__ArucoInfo_Response, distance),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_members = {
  "camera_interface__srv",  // message namespace
  "ArucoInfo_Response",  // message name
  5,  // number of fields
  sizeof(camera_interface__srv__ArucoInfo_Response),
  camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_member_array,  // message members
  camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_type_support_handle = {
  0,
  &camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_camera_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, camera_interface, srv, ArucoInfo_Response)() {
  if (!camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_type_support_handle.typesupport_identifier) {
    camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &camera_interface__srv__ArucoInfo_Response__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "camera_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "camera_interface/srv/detail/aruco_info__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_service_members = {
  "camera_interface__srv",  // service namespace
  "ArucoInfo",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_Request_message_type_support_handle,
  NULL  // response message
  // camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_Response_message_type_support_handle
};

static rosidl_service_type_support_t camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_service_type_support_handle = {
  0,
  &camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, camera_interface, srv, ArucoInfo_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, camera_interface, srv, ArucoInfo_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_camera_interface
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, camera_interface, srv, ArucoInfo)() {
  if (!camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_service_type_support_handle.typesupport_identifier) {
    camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, camera_interface, srv, ArucoInfo_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, camera_interface, srv, ArucoInfo_Response)()->data;
  }

  return &camera_interface__srv__detail__aruco_info__rosidl_typesupport_introspection_c__ArucoInfo_service_type_support_handle;
}
