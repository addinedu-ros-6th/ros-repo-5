// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from taskmanager_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_
#define TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'robot_status'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/RobotStatus in the package taskmanager_msgs.
typedef struct taskmanager_msgs__msg__RobotStatus
{
  rosidl_runtime_c__String robot_status;
  double x;
  double y;
  int64_t battery_status;
} taskmanager_msgs__msg__RobotStatus;

// Struct for a sequence of taskmanager_msgs__msg__RobotStatus.
typedef struct taskmanager_msgs__msg__RobotStatus__Sequence
{
  taskmanager_msgs__msg__RobotStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} taskmanager_msgs__msg__RobotStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_
