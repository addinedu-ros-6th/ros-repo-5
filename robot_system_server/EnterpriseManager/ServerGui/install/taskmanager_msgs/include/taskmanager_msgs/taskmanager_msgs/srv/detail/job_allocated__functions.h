// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from taskmanager_msgs:srv/JobAllocated.idl
// generated code does not contain a copyright notice

#ifndef TASKMANAGER_MSGS__SRV__DETAIL__JOB_ALLOCATED__FUNCTIONS_H_
#define TASKMANAGER_MSGS__SRV__DETAIL__JOB_ALLOCATED__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "taskmanager_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "taskmanager_msgs/srv/detail/job_allocated__struct.h"

/// Initialize srv/JobAllocated message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * taskmanager_msgs__srv__JobAllocated_Request
 * )) before or use
 * taskmanager_msgs__srv__JobAllocated_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Request__init(taskmanager_msgs__srv__JobAllocated_Request * msg);

/// Finalize srv/JobAllocated message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Request__fini(taskmanager_msgs__srv__JobAllocated_Request * msg);

/// Create srv/JobAllocated message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * taskmanager_msgs__srv__JobAllocated_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
taskmanager_msgs__srv__JobAllocated_Request *
taskmanager_msgs__srv__JobAllocated_Request__create();

/// Destroy srv/JobAllocated message.
/**
 * It calls
 * taskmanager_msgs__srv__JobAllocated_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Request__destroy(taskmanager_msgs__srv__JobAllocated_Request * msg);

/// Check for srv/JobAllocated message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Request__are_equal(const taskmanager_msgs__srv__JobAllocated_Request * lhs, const taskmanager_msgs__srv__JobAllocated_Request * rhs);

/// Copy a srv/JobAllocated message.
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
taskmanager_msgs__srv__JobAllocated_Request__copy(
  const taskmanager_msgs__srv__JobAllocated_Request * input,
  taskmanager_msgs__srv__JobAllocated_Request * output);

/// Initialize array of srv/JobAllocated messages.
/**
 * It allocates the memory for the number of elements and calls
 * taskmanager_msgs__srv__JobAllocated_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Request__Sequence__init(taskmanager_msgs__srv__JobAllocated_Request__Sequence * array, size_t size);

/// Finalize array of srv/JobAllocated messages.
/**
 * It calls
 * taskmanager_msgs__srv__JobAllocated_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Request__Sequence__fini(taskmanager_msgs__srv__JobAllocated_Request__Sequence * array);

/// Create array of srv/JobAllocated messages.
/**
 * It allocates the memory for the array and calls
 * taskmanager_msgs__srv__JobAllocated_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
taskmanager_msgs__srv__JobAllocated_Request__Sequence *
taskmanager_msgs__srv__JobAllocated_Request__Sequence__create(size_t size);

/// Destroy array of srv/JobAllocated messages.
/**
 * It calls
 * taskmanager_msgs__srv__JobAllocated_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Request__Sequence__destroy(taskmanager_msgs__srv__JobAllocated_Request__Sequence * array);

/// Check for srv/JobAllocated message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Request__Sequence__are_equal(const taskmanager_msgs__srv__JobAllocated_Request__Sequence * lhs, const taskmanager_msgs__srv__JobAllocated_Request__Sequence * rhs);

/// Copy an array of srv/JobAllocated messages.
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
taskmanager_msgs__srv__JobAllocated_Request__Sequence__copy(
  const taskmanager_msgs__srv__JobAllocated_Request__Sequence * input,
  taskmanager_msgs__srv__JobAllocated_Request__Sequence * output);

/// Initialize srv/JobAllocated message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * taskmanager_msgs__srv__JobAllocated_Response
 * )) before or use
 * taskmanager_msgs__srv__JobAllocated_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Response__init(taskmanager_msgs__srv__JobAllocated_Response * msg);

/// Finalize srv/JobAllocated message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Response__fini(taskmanager_msgs__srv__JobAllocated_Response * msg);

/// Create srv/JobAllocated message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * taskmanager_msgs__srv__JobAllocated_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
taskmanager_msgs__srv__JobAllocated_Response *
taskmanager_msgs__srv__JobAllocated_Response__create();

/// Destroy srv/JobAllocated message.
/**
 * It calls
 * taskmanager_msgs__srv__JobAllocated_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Response__destroy(taskmanager_msgs__srv__JobAllocated_Response * msg);

/// Check for srv/JobAllocated message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Response__are_equal(const taskmanager_msgs__srv__JobAllocated_Response * lhs, const taskmanager_msgs__srv__JobAllocated_Response * rhs);

/// Copy a srv/JobAllocated message.
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
taskmanager_msgs__srv__JobAllocated_Response__copy(
  const taskmanager_msgs__srv__JobAllocated_Response * input,
  taskmanager_msgs__srv__JobAllocated_Response * output);

/// Initialize array of srv/JobAllocated messages.
/**
 * It allocates the memory for the number of elements and calls
 * taskmanager_msgs__srv__JobAllocated_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Response__Sequence__init(taskmanager_msgs__srv__JobAllocated_Response__Sequence * array, size_t size);

/// Finalize array of srv/JobAllocated messages.
/**
 * It calls
 * taskmanager_msgs__srv__JobAllocated_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Response__Sequence__fini(taskmanager_msgs__srv__JobAllocated_Response__Sequence * array);

/// Create array of srv/JobAllocated messages.
/**
 * It allocates the memory for the array and calls
 * taskmanager_msgs__srv__JobAllocated_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
taskmanager_msgs__srv__JobAllocated_Response__Sequence *
taskmanager_msgs__srv__JobAllocated_Response__Sequence__create(size_t size);

/// Destroy array of srv/JobAllocated messages.
/**
 * It calls
 * taskmanager_msgs__srv__JobAllocated_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
void
taskmanager_msgs__srv__JobAllocated_Response__Sequence__destroy(taskmanager_msgs__srv__JobAllocated_Response__Sequence * array);

/// Check for srv/JobAllocated message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_taskmanager_msgs
bool
taskmanager_msgs__srv__JobAllocated_Response__Sequence__are_equal(const taskmanager_msgs__srv__JobAllocated_Response__Sequence * lhs, const taskmanager_msgs__srv__JobAllocated_Response__Sequence * rhs);

/// Copy an array of srv/JobAllocated messages.
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
taskmanager_msgs__srv__JobAllocated_Response__Sequence__copy(
  const taskmanager_msgs__srv__JobAllocated_Response__Sequence * input,
  taskmanager_msgs__srv__JobAllocated_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TASKMANAGER_MSGS__SRV__DETAIL__JOB_ALLOCATED__FUNCTIONS_H_
