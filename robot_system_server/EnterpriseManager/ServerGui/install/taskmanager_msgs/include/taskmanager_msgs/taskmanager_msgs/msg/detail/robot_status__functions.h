// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from taskmanager_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__FUNCTIONS_H_
#define TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "taskmanager_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "taskmanager_msgs/msg/detail/robot_status__struct.h"

/// Initialize msg/RobotStatus message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * taskmanager_msgs__msg__RobotStatus
 * )) before or use
 * taskmanager_msgs__msg__RobotStatus__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__msg__RobotStatus__init(taskmanager_msgs__msg__RobotStatus * msg);

/// Finalize msg/RobotStatus message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__msg__RobotStatus__fini(taskmanager_msgs__msg__RobotStatus * msg);

/// Create msg/RobotStatus message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * taskmanager_msgs__msg__RobotStatus__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
taskmanager_msgs__msg__RobotStatus *
taskmanager_msgs__msg__RobotStatus__create();

/// Destroy msg/RobotStatus message.
/**
 * It calls
 * taskmanager_msgs__msg__RobotStatus__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__msg__RobotStatus__destroy(taskmanager_msgs__msg__RobotStatus * msg);

/// Check for msg/RobotStatus message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__msg__RobotStatus__are_equal(const taskmanager_msgs__msg__RobotStatus * lhs, const taskmanager_msgs__msg__RobotStatus * rhs);

/// Copy a msg/RobotStatus message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__msg__RobotStatus__copy(
  const taskmanager_msgs__msg__RobotStatus * input,
  taskmanager_msgs__msg__RobotStatus * output);

/// Initialize array of msg/RobotStatus messages.
/**
 * It allocates the memory for the number of elements and calls
 * taskmanager_msgs__msg__RobotStatus__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__msg__RobotStatus__Sequence__init(taskmanager_msgs__msg__RobotStatus__Sequence * array, size_t size);

/// Finalize array of msg/RobotStatus messages.
/**
 * It calls
 * taskmanager_msgs__msg__RobotStatus__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__msg__RobotStatus__Sequence__fini(taskmanager_msgs__msg__RobotStatus__Sequence * array);

/// Create array of msg/RobotStatus messages.
/**
 * It allocates the memory for the array and calls
 * taskmanager_msgs__msg__RobotStatus__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
taskmanager_msgs__msg__RobotStatus__Sequence *
taskmanager_msgs__msg__RobotStatus__Sequence__create(size_t size);

/// Destroy array of msg/RobotStatus messages.
/**
 * It calls
 * taskmanager_msgs__msg__RobotStatus__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__msg__RobotStatus__Sequence__destroy(taskmanager_msgs__msg__RobotStatus__Sequence * array);

/// Check for msg/RobotStatus message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__msg__RobotStatus__Sequence__are_equal(const taskmanager_msgs__msg__RobotStatus__Sequence * lhs, const taskmanager_msgs__msg__RobotStatus__Sequence * rhs);

/// Copy an array of msg/RobotStatus messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__msg__RobotStatus__Sequence__copy(
  const taskmanager_msgs__msg__RobotStatus__Sequence * input,
  taskmanager_msgs__msg__RobotStatus__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TASKMANAGER_MSGS__MSG__DETAIL__ROBOT_STATUS__FUNCTIONS_H_