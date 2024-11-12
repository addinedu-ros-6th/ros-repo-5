// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from taskmanager_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice
#include "taskmanager_msgs/msg/detail/robot_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `robot_status`
#include "rosidl_runtime_c/string_functions.h"

bool
taskmanager_msgs__msg__RobotStatus__init(taskmanager_msgs__msg__RobotStatus * msg)
{
  if (!msg) {
    return false;
  }
  // robot_status
  if (!rosidl_runtime_c__String__init(&msg->robot_status)) {
    taskmanager_msgs__msg__RobotStatus__fini(msg);
    return false;
  }
  // x
  // y
  // battery_status
  return true;
}

void
taskmanager_msgs__msg__RobotStatus__fini(taskmanager_msgs__msg__RobotStatus * msg)
{
  if (!msg) {
    return;
  }
  // robot_status
  rosidl_runtime_c__String__fini(&msg->robot_status);
  // x
  // y
  // battery_status
}

bool
taskmanager_msgs__msg__RobotStatus__are_equal(const taskmanager_msgs__msg__RobotStatus * lhs, const taskmanager_msgs__msg__RobotStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->robot_status), &(rhs->robot_status)))
  {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // battery_status
  if (lhs->battery_status != rhs->battery_status) {
    return false;
  }
  return true;
}

bool
taskmanager_msgs__msg__RobotStatus__copy(
  const taskmanager_msgs__msg__RobotStatus * input,
  taskmanager_msgs__msg__RobotStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_status
  if (!rosidl_runtime_c__String__copy(
      &(input->robot_status), &(output->robot_status)))
  {
    return false;
  }
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // battery_status
  output->battery_status = input->battery_status;
  return true;
}

taskmanager_msgs__msg__RobotStatus *
taskmanager_msgs__msg__RobotStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__RobotStatus * msg = (taskmanager_msgs__msg__RobotStatus *)allocator.allocate(sizeof(taskmanager_msgs__msg__RobotStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(taskmanager_msgs__msg__RobotStatus));
  bool success = taskmanager_msgs__msg__RobotStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
taskmanager_msgs__msg__RobotStatus__destroy(taskmanager_msgs__msg__RobotStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    taskmanager_msgs__msg__RobotStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
taskmanager_msgs__msg__RobotStatus__Sequence__init(taskmanager_msgs__msg__RobotStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__RobotStatus * data = NULL;

  if (size) {
    data = (taskmanager_msgs__msg__RobotStatus *)allocator.zero_allocate(size, sizeof(taskmanager_msgs__msg__RobotStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = taskmanager_msgs__msg__RobotStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        taskmanager_msgs__msg__RobotStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
taskmanager_msgs__msg__RobotStatus__Sequence__fini(taskmanager_msgs__msg__RobotStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      taskmanager_msgs__msg__RobotStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

taskmanager_msgs__msg__RobotStatus__Sequence *
taskmanager_msgs__msg__RobotStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__RobotStatus__Sequence * array = (taskmanager_msgs__msg__RobotStatus__Sequence *)allocator.allocate(sizeof(taskmanager_msgs__msg__RobotStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = taskmanager_msgs__msg__RobotStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
taskmanager_msgs__msg__RobotStatus__Sequence__destroy(taskmanager_msgs__msg__RobotStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    taskmanager_msgs__msg__RobotStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
taskmanager_msgs__msg__RobotStatus__Sequence__are_equal(const taskmanager_msgs__msg__RobotStatus__Sequence * lhs, const taskmanager_msgs__msg__RobotStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!taskmanager_msgs__msg__RobotStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
taskmanager_msgs__msg__RobotStatus__Sequence__copy(
  const taskmanager_msgs__msg__RobotStatus__Sequence * input,
  taskmanager_msgs__msg__RobotStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(taskmanager_msgs__msg__RobotStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    taskmanager_msgs__msg__RobotStatus * data =
      (taskmanager_msgs__msg__RobotStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!taskmanager_msgs__msg__RobotStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          taskmanager_msgs__msg__RobotStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!taskmanager_msgs__msg__RobotStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
