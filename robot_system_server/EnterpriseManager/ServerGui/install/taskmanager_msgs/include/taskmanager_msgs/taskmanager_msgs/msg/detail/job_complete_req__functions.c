// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from taskmanager_msgs:msg/JobCompleteReq.idl
// generated code does not contain a copyright notice
#include "taskmanager_msgs/msg/detail/job_complete_req__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
taskmanager_msgs__msg__JobCompleteReq__init(taskmanager_msgs__msg__JobCompleteReq * msg)
{
  if (!msg) {
    return false;
  }
  // job_id
  // job_complete
  // detected_sensor
  return true;
}

void
taskmanager_msgs__msg__JobCompleteReq__fini(taskmanager_msgs__msg__JobCompleteReq * msg)
{
  if (!msg) {
    return;
  }
  // job_id
  // job_complete
  // detected_sensor
}

bool
taskmanager_msgs__msg__JobCompleteReq__are_equal(const taskmanager_msgs__msg__JobCompleteReq * lhs, const taskmanager_msgs__msg__JobCompleteReq * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // job_id
  if (lhs->job_id != rhs->job_id) {
    return false;
  }
  // job_complete
  if (lhs->job_complete != rhs->job_complete) {
    return false;
  }
  // detected_sensor
  if (lhs->detected_sensor != rhs->detected_sensor) {
    return false;
  }
  return true;
}

bool
taskmanager_msgs__msg__JobCompleteReq__copy(
  const taskmanager_msgs__msg__JobCompleteReq * input,
  taskmanager_msgs__msg__JobCompleteReq * output)
{
  if (!input || !output) {
    return false;
  }
  // job_id
  output->job_id = input->job_id;
  // job_complete
  output->job_complete = input->job_complete;
  // detected_sensor
  output->detected_sensor = input->detected_sensor;
  return true;
}

taskmanager_msgs__msg__JobCompleteReq *
taskmanager_msgs__msg__JobCompleteReq__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__JobCompleteReq * msg = (taskmanager_msgs__msg__JobCompleteReq *)allocator.allocate(sizeof(taskmanager_msgs__msg__JobCompleteReq), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(taskmanager_msgs__msg__JobCompleteReq));
  bool success = taskmanager_msgs__msg__JobCompleteReq__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
taskmanager_msgs__msg__JobCompleteReq__destroy(taskmanager_msgs__msg__JobCompleteReq * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    taskmanager_msgs__msg__JobCompleteReq__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
taskmanager_msgs__msg__JobCompleteReq__Sequence__init(taskmanager_msgs__msg__JobCompleteReq__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__JobCompleteReq * data = NULL;

  if (size) {
    data = (taskmanager_msgs__msg__JobCompleteReq *)allocator.zero_allocate(size, sizeof(taskmanager_msgs__msg__JobCompleteReq), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = taskmanager_msgs__msg__JobCompleteReq__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        taskmanager_msgs__msg__JobCompleteReq__fini(&data[i - 1]);
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
taskmanager_msgs__msg__JobCompleteReq__Sequence__fini(taskmanager_msgs__msg__JobCompleteReq__Sequence * array)
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
      taskmanager_msgs__msg__JobCompleteReq__fini(&array->data[i]);
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

taskmanager_msgs__msg__JobCompleteReq__Sequence *
taskmanager_msgs__msg__JobCompleteReq__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__msg__JobCompleteReq__Sequence * array = (taskmanager_msgs__msg__JobCompleteReq__Sequence *)allocator.allocate(sizeof(taskmanager_msgs__msg__JobCompleteReq__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = taskmanager_msgs__msg__JobCompleteReq__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
taskmanager_msgs__msg__JobCompleteReq__Sequence__destroy(taskmanager_msgs__msg__JobCompleteReq__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    taskmanager_msgs__msg__JobCompleteReq__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
taskmanager_msgs__msg__JobCompleteReq__Sequence__are_equal(const taskmanager_msgs__msg__JobCompleteReq__Sequence * lhs, const taskmanager_msgs__msg__JobCompleteReq__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!taskmanager_msgs__msg__JobCompleteReq__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
taskmanager_msgs__msg__JobCompleteReq__Sequence__copy(
  const taskmanager_msgs__msg__JobCompleteReq__Sequence * input,
  taskmanager_msgs__msg__JobCompleteReq__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(taskmanager_msgs__msg__JobCompleteReq);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    taskmanager_msgs__msg__JobCompleteReq * data =
      (taskmanager_msgs__msg__JobCompleteReq *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!taskmanager_msgs__msg__JobCompleteReq__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          taskmanager_msgs__msg__JobCompleteReq__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!taskmanager_msgs__msg__JobCompleteReq__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
