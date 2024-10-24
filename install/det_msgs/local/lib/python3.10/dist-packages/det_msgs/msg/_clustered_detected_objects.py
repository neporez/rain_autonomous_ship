# generated from rosidl_generator_py/resource/_idl.py.em
# with input from det_msgs:msg/ClusteredDetectedObjects.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'bboxes'
# Member 'labels'
# Member 'scores'
# Member 'new_bbox_check'
# Member 'id'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ClusteredDetectedObjects(type):
    """Metaclass of message 'ClusteredDetectedObjects'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('det_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'det_msgs.msg.ClusteredDetectedObjects')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__clustered_detected_objects
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__clustered_detected_objects
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__clustered_detected_objects
            cls._TYPE_SUPPORT = module.type_support_msg__msg__clustered_detected_objects
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__clustered_detected_objects

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ClusteredDetectedObjects(metaclass=Metaclass_ClusteredDetectedObjects):
    """Message class 'ClusteredDetectedObjects'."""

    __slots__ = [
        '_bboxes',
        '_bboxes_num',
        '_labels',
        '_scores',
        '_new_bbox_check',
        '_id',
        '_pose',
    ]

    _fields_and_field_types = {
        'bboxes': 'sequence<float>',
        'bboxes_num': 'uint32',
        'labels': 'sequence<int32>',
        'scores': 'sequence<float>',
        'new_bbox_check': 'sequence<int32>',
        'id': 'sequence<int32>',
        'pose': 'geometry_msgs/Pose',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.bboxes = array.array('f', kwargs.get('bboxes', []))
        self.bboxes_num = kwargs.get('bboxes_num', int())
        self.labels = array.array('i', kwargs.get('labels', []))
        self.scores = array.array('f', kwargs.get('scores', []))
        self.new_bbox_check = array.array('i', kwargs.get('new_bbox_check', []))
        self.id = array.array('i', kwargs.get('id', []))
        from geometry_msgs.msg import Pose
        self.pose = kwargs.get('pose', Pose())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.bboxes != other.bboxes:
            return False
        if self.bboxes_num != other.bboxes_num:
            return False
        if self.labels != other.labels:
            return False
        if self.scores != other.scores:
            return False
        if self.new_bbox_check != other.new_bbox_check:
            return False
        if self.id != other.id:
            return False
        if self.pose != other.pose:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def bboxes(self):
        """Message field 'bboxes'."""
        return self._bboxes

    @bboxes.setter
    def bboxes(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'bboxes' array.array() must have the type code of 'f'"
            self._bboxes = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'bboxes' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._bboxes = array.array('f', value)

    @builtins.property
    def bboxes_num(self):
        """Message field 'bboxes_num'."""
        return self._bboxes_num

    @bboxes_num.setter
    def bboxes_num(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'bboxes_num' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'bboxes_num' field must be an unsigned integer in [0, 4294967295]"
        self._bboxes_num = value

    @builtins.property
    def labels(self):
        """Message field 'labels'."""
        return self._labels

    @labels.setter
    def labels(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'labels' array.array() must have the type code of 'i'"
            self._labels = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'labels' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._labels = array.array('i', value)

    @builtins.property
    def scores(self):
        """Message field 'scores'."""
        return self._scores

    @scores.setter
    def scores(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'scores' array.array() must have the type code of 'f'"
            self._scores = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'scores' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._scores = array.array('f', value)

    @builtins.property
    def new_bbox_check(self):
        """Message field 'new_bbox_check'."""
        return self._new_bbox_check

    @new_bbox_check.setter
    def new_bbox_check(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'new_bbox_check' array.array() must have the type code of 'i'"
            self._new_bbox_check = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'new_bbox_check' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._new_bbox_check = array.array('i', value)

    @builtins.property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'id' array.array() must have the type code of 'i'"
            self._id = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'id' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._id = array.array('i', value)

    @builtins.property
    def pose(self):
        """Message field 'pose'."""
        return self._pose

    @pose.setter
    def pose(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'pose' field must be a sub message of type 'Pose'"
        self._pose = value
