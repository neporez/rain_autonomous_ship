// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from det_msgs:msg/ClusteredDetectedObjects.idl
// generated code does not contain a copyright notice

#ifndef DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__FUNCTIONS_H_
#define DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "det_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "det_msgs/msg/detail/clustered_detected_objects__struct.h"

/// Initialize msg/ClusteredDetectedObjects message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * det_msgs__msg__ClusteredDetectedObjects
 * )) before or use
 * det_msgs__msg__ClusteredDetectedObjects__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
bool
det_msgs__msg__ClusteredDetectedObjects__init(det_msgs__msg__ClusteredDetectedObjects * msg);

/// Finalize msg/ClusteredDetectedObjects message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
void
det_msgs__msg__ClusteredDetectedObjects__fini(det_msgs__msg__ClusteredDetectedObjects * msg);

/// Create msg/ClusteredDetectedObjects message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * det_msgs__msg__ClusteredDetectedObjects__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
det_msgs__msg__ClusteredDetectedObjects *
det_msgs__msg__ClusteredDetectedObjects__create();

/// Destroy msg/ClusteredDetectedObjects message.
/**
 * It calls
 * det_msgs__msg__ClusteredDetectedObjects__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
void
det_msgs__msg__ClusteredDetectedObjects__destroy(det_msgs__msg__ClusteredDetectedObjects * msg);

/// Check for msg/ClusteredDetectedObjects message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
bool
det_msgs__msg__ClusteredDetectedObjects__are_equal(const det_msgs__msg__ClusteredDetectedObjects * lhs, const det_msgs__msg__ClusteredDetectedObjects * rhs);

/// Copy a msg/ClusteredDetectedObjects message.
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
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
bool
det_msgs__msg__ClusteredDetectedObjects__copy(
  const det_msgs__msg__ClusteredDetectedObjects * input,
  det_msgs__msg__ClusteredDetectedObjects * output);

/// Initialize array of msg/ClusteredDetectedObjects messages.
/**
 * It allocates the memory for the number of elements and calls
 * det_msgs__msg__ClusteredDetectedObjects__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
bool
det_msgs__msg__ClusteredDetectedObjects__Sequence__init(det_msgs__msg__ClusteredDetectedObjects__Sequence * array, size_t size);

/// Finalize array of msg/ClusteredDetectedObjects messages.
/**
 * It calls
 * det_msgs__msg__ClusteredDetectedObjects__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
void
det_msgs__msg__ClusteredDetectedObjects__Sequence__fini(det_msgs__msg__ClusteredDetectedObjects__Sequence * array);

/// Create array of msg/ClusteredDetectedObjects messages.
/**
 * It allocates the memory for the array and calls
 * det_msgs__msg__ClusteredDetectedObjects__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
det_msgs__msg__ClusteredDetectedObjects__Sequence *
det_msgs__msg__ClusteredDetectedObjects__Sequence__create(size_t size);

/// Destroy array of msg/ClusteredDetectedObjects messages.
/**
 * It calls
 * det_msgs__msg__ClusteredDetectedObjects__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
void
det_msgs__msg__ClusteredDetectedObjects__Sequence__destroy(det_msgs__msg__ClusteredDetectedObjects__Sequence * array);

/// Check for msg/ClusteredDetectedObjects message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
bool
det_msgs__msg__ClusteredDetectedObjects__Sequence__are_equal(const det_msgs__msg__ClusteredDetectedObjects__Sequence * lhs, const det_msgs__msg__ClusteredDetectedObjects__Sequence * rhs);

/// Copy an array of msg/ClusteredDetectedObjects messages.
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
ROSIDL_GENERATOR_C_PUBLIC_det_msgs
bool
det_msgs__msg__ClusteredDetectedObjects__Sequence__copy(
  const det_msgs__msg__ClusteredDetectedObjects__Sequence * input,
  det_msgs__msg__ClusteredDetectedObjects__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // DET_MSGS__MSG__DETAIL__CLUSTERED_DETECTED_OBJECTS__FUNCTIONS_H_
