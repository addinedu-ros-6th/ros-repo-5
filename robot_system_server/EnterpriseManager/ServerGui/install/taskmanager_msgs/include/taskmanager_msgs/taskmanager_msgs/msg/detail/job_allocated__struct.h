// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from taskmanager_msgs:msg/JobAllocated.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__STRUCT_H_
#define TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/JobAllocated in the package taskmanager_msgs.
typedef struct taskmanager_msgs__msg__JobAllocated
{
  int64_t robot_num;
  double x;
  double y;
  double z;
  double w;
  int64_t job_id;
  int64_t nav_id;
} taskmanager_msgs__msg__JobAllocated;

// Struct for a sequence of taskmanager_msgs__msg__JobAllocated.
typedef struct taskmanager_msgs__msg__JobAllocated__Sequence
{
  taskmanager_msgs__msg__JobAllocated * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} taskmanager_msgs__msg__JobAllocated__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__JOB_ALLOCATED__STRUCT_H_
