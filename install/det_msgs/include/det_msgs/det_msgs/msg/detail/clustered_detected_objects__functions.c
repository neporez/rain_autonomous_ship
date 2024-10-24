// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from det_msgs:msg/ClusteredDetectedObjects.idl
// generated code does not contain a copyright notice
#include "det_msgs/msg/detail/clustered_detected_objects__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `bboxes`
// Member `labels`
// Member `scores`
// Member `new_bbox_check`
// Member `id`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
det_msgs__msg__ClusteredDetectedObjects__init(det_msgs__msg__ClusteredDetectedObjects * msg)
{
  if (!msg) {
    return false;
  }
  // bboxes
  if (!rosidl_runtime_c__float__Sequence__init(&msg->bboxes, 0)) {
    det_msgs__msg__ClusteredDetectedObjects__fini(msg);
    return false;
  }
  // bboxes_num
  // labels
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->labels, 0)) {
    det_msgs__msg__ClusteredDetectedObjects__fini(msg);
    return false;
  }
  // scores
  if (!rosidl_runtime_c__float__Sequence__init(&msg->scores, 0)) {
    det_msgs__msg__ClusteredDetectedObjects__fini(msg);
    return false;
  }
  // new_bbox_check
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->new_bbox_check, 0)) {
    det_msgs__msg__ClusteredDetectedObjects__fini(msg);
    return false;
  }
  // id
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->id, 0)) {
    det_msgs__msg__ClusteredDetectedObjects__fini(msg);
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__init(&msg->pose)) {
    det_msgs__msg__ClusteredDetectedObjects__fini(msg);
    return false;
  }
  return true;
}

void
det_msgs__msg__ClusteredDetectedObjects__fini(det_msgs__msg__ClusteredDetectedObjects * msg)
{
  if (!msg) {
    return;
  }
  // bboxes
  rosidl_runtime_c__float__Sequence__fini(&msg->bboxes);
  // bboxes_num
  // labels
  rosidl_runtime_c__int32__Sequence__fini(&msg->labels);
  // scores
  rosidl_runtime_c__float__Sequence__fini(&msg->scores);
  // new_bbox_check
  rosidl_runtime_c__int32__Sequence__fini(&msg->new_bbox_check);
  // id
  rosidl_runtime_c__int32__Sequence__fini(&msg->id);
  // pose
  geometry_msgs__msg__Pose__fini(&msg->pose);
}

bool
det_msgs__msg__ClusteredDetectedObjects__are_equal(const det_msgs__msg__ClusteredDetectedObjects * lhs, const det_msgs__msg__ClusteredDetectedObjects * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // bboxes
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->bboxes), &(rhs->bboxes)))
  {
    return false;
  }
  // bboxes_num
  if (lhs->bboxes_num != rhs->bboxes_num) {
    return false;
  }
  // labels
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->labels), &(rhs->labels)))
  {
    return false;
  }
  // scores
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->scores), &(rhs->scores)))
  {
    return false;
  }
  // new_bbox_check
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->new_bbox_check), &(rhs->new_bbox_check)))
  {
    return false;
  }
  // id
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->id), &(rhs->id)))
  {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  return true;
}

bool
det_msgs__msg__ClusteredDetectedObjects__copy(
  const det_msgs__msg__ClusteredDetectedObjects * input,
  det_msgs__msg__ClusteredDetectedObjects * output)
{
  if (!input || !output) {
    return false;
  }
  // bboxes
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->bboxes), &(output->bboxes)))
  {
    return false;
  }
  // bboxes_num
  output->bboxes_num = input->bboxes_num;
  // labels
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->labels), &(output->labels)))
  {
    return false;
  }
  // scores
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->scores), &(output->scores)))
  {
    return false;
  }
  // new_bbox_check
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->new_bbox_check), &(output->new_bbox_check)))
  {
    return false;
  }
  // id
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->id), &(output->id)))
  {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  return true;
}

det_msgs__msg__ClusteredDetectedObjects *
det_msgs__msg__ClusteredDetectedObjects__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  det_msgs__msg__ClusteredDetectedObjects * msg = (det_msgs__msg__ClusteredDetectedObjects *)allocator.allocate(sizeof(det_msgs__msg__ClusteredDetectedObjects), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(det_msgs__msg__ClusteredDetectedObjects));
  bool success = det_msgs__msg__ClusteredDetectedObjects__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
det_msgs__msg__ClusteredDetectedObjects__destroy(det_msgs__msg__ClusteredDetectedObjects * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    det_msgs__msg__ClusteredDetectedObjects__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
det_msgs__msg__ClusteredDetectedObjects__Sequence__init(det_msgs__msg__ClusteredDetectedObjects__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  det_msgs__msg__ClusteredDetectedObjects * data = NULL;

  if (size) {
    data = (det_msgs__msg__ClusteredDetectedObjects *)allocator.zero_allocate(size, sizeof(det_msgs__msg__ClusteredDetectedObjects), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = det_msgs__msg__ClusteredDetectedObjects__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        det_msgs__msg__ClusteredDetectedObjects__fini(&data[i - 1]);
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
det_msgs__msg__ClusteredDetectedObjects__Sequence__fini(det_msgs__msg__ClusteredDetectedObjects__Sequence * array)
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
      det_msgs__msg__ClusteredDetectedObjects__fini(&array->data[i]);
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

det_msgs__msg__ClusteredDetectedObjects__Sequence *
det_msgs__msg__ClusteredDetectedObjects__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  det_msgs__msg__ClusteredDetectedObjects__Sequence * array = (det_msgs__msg__ClusteredDetectedObjects__Sequence *)allocator.allocate(sizeof(det_msgs__msg__ClusteredDetectedObjects__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = det_msgs__msg__ClusteredDetectedObjects__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
det_msgs__msg__ClusteredDetectedObjects__Sequence__destroy(det_msgs__msg__ClusteredDetectedObjects__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    det_msgs__msg__ClusteredDetectedObjects__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
det_msgs__msg__ClusteredDetectedObjects__Sequence__are_equal(const det_msgs__msg__ClusteredDetectedObjects__Sequence * lhs, const det_msgs__msg__ClusteredDetectedObjects__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!det_msgs__msg__ClusteredDetectedObjects__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
det_msgs__msg__ClusteredDetectedObjects__Sequence__copy(
  const det_msgs__msg__ClusteredDetectedObjects__Sequence * input,
  det_msgs__msg__ClusteredDetectedObjects__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(det_msgs__msg__ClusteredDetectedObjects);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    det_msgs__msg__ClusteredDetectedObjects * data =
      (det_msgs__msg__ClusteredDetectedObjects *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!det_msgs__msg__ClusteredDetectedObjects__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          det_msgs__msg__ClusteredDetectedObjects__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!det_msgs__msg__ClusteredDetectedObjects__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
