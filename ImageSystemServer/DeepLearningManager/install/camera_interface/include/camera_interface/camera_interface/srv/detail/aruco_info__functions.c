// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from camera_interface:srv/ArucoInfo.idl
// generated code does not contain a copyright notice
#include "camera_interface/srv/detail/aruco_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
camera_interface__srv__ArucoInfo_Request__init(camera_interface__srv__ArucoInfo_Request * msg)
{
  if (!msg) {
    return false;
  }
  // aruco_info_req
  return true;
}

void
camera_interface__srv__ArucoInfo_Request__fini(camera_interface__srv__ArucoInfo_Request * msg)
{
  if (!msg) {
    return;
  }
  // aruco_info_req
}

bool
camera_interface__srv__ArucoInfo_Request__are_equal(const camera_interface__srv__ArucoInfo_Request * lhs, const camera_interface__srv__ArucoInfo_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // aruco_info_req
  if (lhs->aruco_info_req != rhs->aruco_info_req) {
    return false;
  }
  return true;
}

bool
camera_interface__srv__ArucoInfo_Request__copy(
  const camera_interface__srv__ArucoInfo_Request * input,
  camera_interface__srv__ArucoInfo_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // aruco_info_req
  output->aruco_info_req = input->aruco_info_req;
  return true;
}

camera_interface__srv__ArucoInfo_Request *
camera_interface__srv__ArucoInfo_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  camera_interface__srv__ArucoInfo_Request * msg = (camera_interface__srv__ArucoInfo_Request *)allocator.allocate(sizeof(camera_interface__srv__ArucoInfo_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(camera_interface__srv__ArucoInfo_Request));
  bool success = camera_interface__srv__ArucoInfo_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
camera_interface__srv__ArucoInfo_Request__destroy(camera_interface__srv__ArucoInfo_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    camera_interface__srv__ArucoInfo_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
camera_interface__srv__ArucoInfo_Request__Sequence__init(camera_interface__srv__ArucoInfo_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  camera_interface__srv__ArucoInfo_Request * data = NULL;

  if (size) {
    data = (camera_interface__srv__ArucoInfo_Request *)allocator.zero_allocate(size, sizeof(camera_interface__srv__ArucoInfo_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = camera_interface__srv__ArucoInfo_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        camera_interface__srv__ArucoInfo_Request__fini(&data[i - 1]);
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
camera_interface__srv__ArucoInfo_Request__Sequence__fini(camera_interface__srv__ArucoInfo_Request__Sequence * array)
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
      camera_interface__srv__ArucoInfo_Request__fini(&array->data[i]);
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

camera_interface__srv__ArucoInfo_Request__Sequence *
camera_interface__srv__ArucoInfo_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  camera_interface__srv__ArucoInfo_Request__Sequence * array = (camera_interface__srv__ArucoInfo_Request__Sequence *)allocator.allocate(sizeof(camera_interface__srv__ArucoInfo_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = camera_interface__srv__ArucoInfo_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
camera_interface__srv__ArucoInfo_Request__Sequence__destroy(camera_interface__srv__ArucoInfo_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    camera_interface__srv__ArucoInfo_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
camera_interface__srv__ArucoInfo_Request__Sequence__are_equal(const camera_interface__srv__ArucoInfo_Request__Sequence * lhs, const camera_interface__srv__ArucoInfo_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!camera_interface__srv__ArucoInfo_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
camera_interface__srv__ArucoInfo_Request__Sequence__copy(
  const camera_interface__srv__ArucoInfo_Request__Sequence * input,
  camera_interface__srv__ArucoInfo_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(camera_interface__srv__ArucoInfo_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    camera_interface__srv__ArucoInfo_Request * data =
      (camera_interface__srv__ArucoInfo_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!camera_interface__srv__ArucoInfo_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          camera_interface__srv__ArucoInfo_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!camera_interface__srv__ArucoInfo_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
camera_interface__srv__ArucoInfo_Response__init(camera_interface__srv__ArucoInfo_Response * msg)
{
  if (!msg) {
    return false;
  }
  // aruco_id
  // pos_x
  // pos_y
  // pos_z
  // distance
  return true;
}

void
camera_interface__srv__ArucoInfo_Response__fini(camera_interface__srv__ArucoInfo_Response * msg)
{
  if (!msg) {
    return;
  }
  // aruco_id
  // pos_x
  // pos_y
  // pos_z
  // distance
}

bool
camera_interface__srv__ArucoInfo_Response__are_equal(const camera_interface__srv__ArucoInfo_Response * lhs, const camera_interface__srv__ArucoInfo_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // aruco_id
  if (lhs->aruco_id != rhs->aruco_id) {
    return false;
  }
  // pos_x
  if (lhs->pos_x != rhs->pos_x) {
    return false;
  }
  // pos_y
  if (lhs->pos_y != rhs->pos_y) {
    return false;
  }
  // pos_z
  if (lhs->pos_z != rhs->pos_z) {
    return false;
  }
  // distance
  if (lhs->distance != rhs->distance) {
    return false;
  }
  return true;
}

bool
camera_interface__srv__ArucoInfo_Response__copy(
  const camera_interface__srv__ArucoInfo_Response * input,
  camera_interface__srv__ArucoInfo_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // aruco_id
  output->aruco_id = input->aruco_id;
  // pos_x
  output->pos_x = input->pos_x;
  // pos_y
  output->pos_y = input->pos_y;
  // pos_z
  output->pos_z = input->pos_z;
  // distance
  output->distance = input->distance;
  return true;
}

camera_interface__srv__ArucoInfo_Response *
camera_interface__srv__ArucoInfo_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  camera_interface__srv__ArucoInfo_Response * msg = (camera_interface__srv__ArucoInfo_Response *)allocator.allocate(sizeof(camera_interface__srv__ArucoInfo_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(camera_interface__srv__ArucoInfo_Response));
  bool success = camera_interface__srv__ArucoInfo_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
camera_interface__srv__ArucoInfo_Response__destroy(camera_interface__srv__ArucoInfo_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    camera_interface__srv__ArucoInfo_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
camera_interface__srv__ArucoInfo_Response__Sequence__init(camera_interface__srv__ArucoInfo_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  camera_interface__srv__ArucoInfo_Response * data = NULL;

  if (size) {
    data = (camera_interface__srv__ArucoInfo_Response *)allocator.zero_allocate(size, sizeof(camera_interface__srv__ArucoInfo_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = camera_interface__srv__ArucoInfo_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        camera_interface__srv__ArucoInfo_Response__fini(&data[i - 1]);
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
camera_interface__srv__ArucoInfo_Response__Sequence__fini(camera_interface__srv__ArucoInfo_Response__Sequence * array)
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
      camera_interface__srv__ArucoInfo_Response__fini(&array->data[i]);
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

camera_interface__srv__ArucoInfo_Response__Sequence *
camera_interface__srv__ArucoInfo_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  camera_interface__srv__ArucoInfo_Response__Sequence * array = (camera_interface__srv__ArucoInfo_Response__Sequence *)allocator.allocate(sizeof(camera_interface__srv__ArucoInfo_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = camera_interface__srv__ArucoInfo_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
camera_interface__srv__ArucoInfo_Response__Sequence__destroy(camera_interface__srv__ArucoInfo_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    camera_interface__srv__ArucoInfo_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
camera_interface__srv__ArucoInfo_Response__Sequence__are_equal(const camera_interface__srv__ArucoInfo_Response__Sequence * lhs, const camera_interface__srv__ArucoInfo_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!camera_interface__srv__ArucoInfo_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
camera_interface__srv__ArucoInfo_Response__Sequence__copy(
  const camera_interface__srv__ArucoInfo_Response__Sequence * input,
  camera_interface__srv__ArucoInfo_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(camera_interface__srv__ArucoInfo_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    camera_interface__srv__ArucoInfo_Response * data =
      (camera_interface__srv__ArucoInfo_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!camera_interface__srv__ArucoInfo_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          camera_interface__srv__ArucoInfo_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!camera_interface__srv__ArucoInfo_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
