// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from taskmanager_msgs:msg/JobAllocated.idl
// generated code does not contain a copyright notice
#include "taskmanager_msgs/msg/detail/job_allocated__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
taskmanager_msgs__msg__JobAllocated__init(taskmanager_msgs__msg__JobAllocated * msg)
{
  if (!msg) {
    return false;
  }
  // robot_num
  // x
  // y
  // z
  // w
  // job_id
  // nav_id
  return true;
}

void
taskmanager_msgs__msg__JobAllocated__fini(taskmanager_msgs__msg__JobAllocated * msg)
{
  if (!msg) {
    return;
  }
  // robot_num
  // x
  // y
  // z
  // w
  // job_id
  // nav_id
}

bool
taskmanager_msgs__msg__JobAllocated__are_equal(const taskmanager_msgs__msg__JobAllocated * lhs, const taskmanager_msgs__msg__JobAllocated * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_num
  if (lhs->robot_num != rhs->robot_num) {
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
  // z
  if (lhs->z != rhs->z) {
    return false;
  }
  // w
  if (lhs->w != rhs->w) {
    return false;
  }
  // job_id
  if (lhs->job_id != rhs->job_id) {
    return false;
  }
  // nav_id
  if (lhs->nav_id != rhs->nav_id) {
    return false;
  }
  return true;
}

bool
taskmanager_msgs__msg__JobAllocated__copy(
  const taskmanager_msgs__msg__JobAllocated * input,
  taskmanager_msgs__msg__JobAllocated * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_num
  output->robot_num = input->robot_num;
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // z
  output->z = input->z;
  // w
  output->w = input->w;
  // job_id
  output->job_id = input->job_id;
  // nav_id
  output->nav_id = input->nav_id;
  return true;
}

taskmanager_msgs__msg__JobAllocated *
taskmanager_msgs__msg__JobAllocated__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__JobAllocated * msg = (taskmanager_msgs__msg__JobAllocated *)allocator.allocate(sizeof(taskmanager_msgs__msg__JobAllocated), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(taskmanager_msgs__msg__JobAllocated));
  bool success = taskmanager_msgs__msg__JobAllocated__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
taskmanager_msgs__msg__JobAllocated__destroy(taskmanager_msgs__msg__JobAllocated * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    taskmanager_msgs__msg__JobAllocated__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
taskmanager_msgs__msg__JobAllocated__Sequence__init(taskmanager_msgs__msg__JobAllocated__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__JobAllocated * data = NULL;

  if (size) {
    data = (taskmanager_msgs__msg__JobAllocated *)allocator.zero_allocate(size, sizeof(taskmanager_msgs__msg__JobAllocated), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = taskmanager_msgs__msg__JobAllocated__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        taskmanager_msgs__msg__JobAllocated__fini(&data[i - 1]);
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
taskmanager_msgs__msg__JobAllocated__Sequence__fini(taskmanager_msgs__msg__JobAllocated__Sequence * array)
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
      taskmanager_msgs__msg__JobAllocated__fini(&array->data[i]);
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

taskmanager_msgs__msg__JobAllocated__Sequence *
taskmanager_msgs__msg__JobAllocated__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__JobAllocated__Sequence * array = (taskmanager_msgs__msg__JobAllocated__Sequence *)allocator.allocate(sizeof(taskmanager_msgs__msg__JobAllocated__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = taskmanager_msgs__msg__JobAllocated__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
taskmanager_msgs__msg__JobAllocated__Sequence__destroy(taskmanager_msgs__msg__JobAllocated__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    taskmanager_msgs__msg__JobAllocated__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
taskmanager_msgs__msg__JobAllocated__Sequence__are_equal(const taskmanager_msgs__msg__JobAllocated__Sequence * lhs, const taskmanager_msgs__msg__JobAllocated__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!taskmanager_msgs__msg__JobAllocated__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
taskmanager_msgs__msg__JobAllocated__Sequence__copy(
  const taskmanager_msgs__msg__JobAllocated__Sequence * input,
  taskmanager_msgs__msg__JobAllocated__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(taskmanager_msgs__msg__JobAllocated);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    taskmanager_msgs__msg__JobAllocated * data =
      (taskmanager_msgs__msg__JobAllocated *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!taskmanager_msgs__msg__JobAllocated__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          taskmanager_msgs__msg__JobAllocated__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!taskmanager_msgs__msg__JobAllocated__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
