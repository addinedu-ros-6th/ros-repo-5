// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from taskmanager_msgs:msg/JobAllocated.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "taskmanager_msgs/msg/detail/job_allocated__rosidl_typesupport_introspection_c.h"
#include "taskmanager_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "taskmanager_msgs/msg/detail/job_allocated__functions.h"
#include "taskmanager_msgs/msg/detail/job_allocated__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  taskmanager_msgs__msg__JobAllocated__init(message_memory);
}

void taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_fini_function(void * message_memory)
{
  taskmanager_msgs__msg__JobAllocated__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_member_array[7] = {
  {
    "robot_num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(taskmanager_msgs__msg__JobAllocated, robot_num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(taskmanager_msgs__msg__JobAllocated, x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(taskmanager_msgs__msg__JobAllocated, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(taskmanager_msgs__msg__JobAllocated, z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "w",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(taskmanager_msgs__msg__JobAllocated, w),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "job_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(taskmanager_msgs__msg__JobAllocated, job_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "nav_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(taskmanager_msgs__msg__JobAllocated, nav_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_members = {
  "taskmanager_msgs__msg",  // message namespace
  "JobAllocated",  // message name
  7,  // number of fields
  sizeof(taskmanager_msgs__msg__JobAllocated),
  taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_member_array,  // message members
  taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_init_function,  // function to initialize message memory (memory has to be allocated)
  taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_type_support_handle = {
  0,
  &taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_taskmanager_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, taskmanager_msgs, msg, JobAllocated)() {
  if (!taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_type_support_handle.typesupport_identifier) {
    taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &taskmanager_msgs__msg__JobAllocated__rosidl_typesupport_introspection_c__JobAllocated_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
