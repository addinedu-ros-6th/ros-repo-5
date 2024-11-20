// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from taskmanager_msgs:msg/JobCompleteReq.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__JOB_COMPLETE_REQ__STRUCT_H_
#define TASKMANAGER_MSGS__MSG__DETAIL__JOB_COMPLETE_REQ__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/JobCompleteReq in the package taskmanager_msgs.
typedef struct taskmanager_msgs__msg__JobCompleteReq
{
  int64_t job_id;
  int64_t job_complete;
  int64_t detected_sensor;
} taskmanager_msgs__msg__JobCompleteReq;

// Struct for a sequence of taskmanager_msgs__msg__JobCompleteReq.
typedef struct taskmanager_msgs__msg__JobCompleteReq__Sequence
{
  taskmanager_msgs__msg__JobCompleteReq * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} taskmanager_msgs__msg__JobCompleteReq__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__JOB_COMPLETE_REQ__STRUCT_H_
