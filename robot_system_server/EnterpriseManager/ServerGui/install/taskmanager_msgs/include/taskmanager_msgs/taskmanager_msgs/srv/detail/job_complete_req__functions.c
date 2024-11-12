// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from taskmanager_msgs:srv/JobCompleteReq.idl
// generated code does not contain a copyright notice
#include "taskmanager_msgs/srv/detail/job_complete_req__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
taskmanager_msgs__srv__JobCompleteReq_Request__init(taskmanager_msgs__srv__JobCompleteReq_Request * msg)
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
taskmanager_msgs__srv__JobCompleteReq_Request__fini(taskmanager_msgs__srv__JobCompleteReq_Request * msg)
{
  if (!msg) {
    return;
  }
  // job_id
  // job_complete
  // detected_sensor
}

bool
taskmanager_msgs__srv__JobCompleteReq_Request__are_equal(const taskmanager_msgs__srv__JobCompleteReq_Request * lhs, const taskmanager_msgs__srv__JobCompleteReq_Request * rhs)
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
taskmanager_msgs__srv__JobCompleteReq_Request__copy(
  const taskmanager_msgs__srv__JobCompleteReq_Request * input,
  taskmanager_msgs__srv__JobCompleteReq_Request * output)
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

taskmanager_msgs__srv__JobCompleteReq_Request *
taskmanager_msgs__srv__JobCompleteReq_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__srv__JobCompleteReq_Request * msg = (taskmanager_msgs__srv__JobCompleteReq_Request *)allocator.allocate(sizeof(taskmanager_msgs__srv__JobCompleteReq_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(taskmanager_msgs__srv__JobCompleteReq_Request));
  bool success = taskmanager_msgs__srv__JobCompleteReq_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
taskmanager_msgs__srv__JobCompleteReq_Request__destroy(taskmanager_msgs__srv__JobCompleteReq_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    taskmanager_msgs__srv__JobCompleteReq_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__init(taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__srv__JobCompleteReq_Request * data = NULL;

  if (size) {
    data = (taskmanager_msgs__srv__JobCompleteReq_Request *)allocator.zero_allocate(size, sizeof(taskmanager_msgs__srv__JobCompleteReq_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = taskmanager_msgs__srv__JobCompleteReq_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        taskmanager_msgs__srv__JobCompleteReq_Request__fini(&data[i - 1]);
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
taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__fini(taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * array)
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
      taskmanager_msgs__srv__JobCompleteReq_Request__fini(&array->data[i]);
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

taskmanager_msgs__srv__JobCompleteReq_Request__Sequence *
taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * array = (taskmanager_msgs__srv__JobCompleteReq_Request__Sequence *)allocator.allocate(sizeof(taskmanager_msgs__srv__JobCompleteReq_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__destroy(taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__are_equal(const taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * lhs, const taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!taskmanager_msgs__srv__JobCompleteReq_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
taskmanager_msgs__srv__JobCompleteReq_Request__Sequence__copy(
  const taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * input,
  taskmanager_msgs__srv__JobCompleteReq_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(taskmanager_msgs__srv__JobCompleteReq_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    taskmanager_msgs__srv__JobCompleteReq_Request * data =
      (taskmanager_msgs__srv__JobCompleteReq_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!taskmanager_msgs__srv__JobCompleteReq_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          taskmanager_msgs__srv__JobCompleteReq_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!taskmanager_msgs__srv__JobCompleteReq_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
taskmanager_msgs__srv__JobCompleteReq_Response__init(taskmanager_msgs__srv__JobCompleteReq_Response * msg)
{
  if (!msg) {
    return false;
  }
  // receive_complete
  return true;
}

void
taskmanager_msgs__srv__JobCompleteReq_Response__fini(taskmanager_msgs__srv__JobCompleteReq_Response * msg)
{
  if (!msg) {
    return;
  }
  // receive_complete
}

bool
taskmanager_msgs__srv__JobCompleteReq_Response__are_equal(const taskmanager_msgs__srv__JobCompleteReq_Response * lhs, const taskmanager_msgs__srv__JobCompleteReq_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // receive_complete
  if (lhs->receive_complete != rhs->receive_complete) {
    return false;
  }
  return true;
}

bool
taskmanager_msgs__srv__JobCompleteReq_Response__copy(
  const taskmanager_msgs__srv__JobCompleteReq_Response * input,
  taskmanager_msgs__srv__JobCompleteReq_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // receive_complete
  output->receive_complete = input->receive_complete;
  return true;
}

taskmanager_msgs__srv__JobCompleteReq_Response *
taskmanager_msgs__srv__JobCompleteReq_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__srv__JobCompleteReq_Response * msg = (taskmanager_msgs__srv__JobCompleteReq_Response *)allocator.allocate(sizeof(taskmanager_msgs__srv__JobCompleteReq_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(taskmanager_msgs__srv__JobCompleteReq_Response));
  bool success = taskmanager_msgs__srv__JobCompleteReq_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
taskmanager_msgs__srv__JobCompleteReq_Response__destroy(taskmanager_msgs__srv__JobCompleteReq_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    taskmanager_msgs__srv__JobCompleteReq_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__init(taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__srv__JobCompleteReq_Response * data = NULL;

  if (size) {
    data = (taskmanager_msgs__srv__JobCompleteReq_Response *)allocator.zero_allocate(size, sizeof(taskmanager_msgs__srv__JobCompleteReq_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = taskmanager_msgs__srv__JobCompleteReq_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        taskmanager_msgs__srv__JobCompleteReq_Response__fini(&data[i - 1]);
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
taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__fini(taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * array)
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
      taskmanager_msgs__srv__JobCompleteReq_Response__fini(&array->data[i]);
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

taskmanager_msgs__srv__JobCompleteReq_Response__Sequence *
taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * array = (taskmanager_msgs__srv__JobCompleteReq_Response__Sequence *)allocator.allocate(sizeof(taskmanager_msgs__srv__JobCompleteReq_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__destroy(taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__are_equal(const taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * lhs, const taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!taskmanager_msgs__srv__JobCompleteReq_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
taskmanager_msgs__srv__JobCompleteReq_Response__Sequence__copy(
  const taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * input,
  taskmanager_msgs__srv__JobCompleteReq_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(taskmanager_msgs__srv__JobCompleteReq_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    taskmanager_msgs__srv__JobCompleteReq_Response * data =
      (taskmanager_msgs__srv__JobCompleteReq_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!taskmanager_msgs__srv__JobCompleteReq_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          taskmanager_msgs__srv__JobCompleteReq_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!taskmanager_msgs__srv__JobCompleteReq_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
