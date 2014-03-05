from .exceptions import DeserializationError
from .constants import (
    MAX_INT8, MIN_INT8, MAX_INT16, MIN_INT16, MAX_INT32, MIN_INT32, MAX_INT64,
    MIN_INT64, MAX_UINT8, MAX_UINT16, MAX_UINT32, MAX_UINT64,
)


def deserialize_int8(x):
    """Deserialize 8-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to signed 8-bit '
                                   'integer' % (x))
    if x < MIN_INT8 or x > MAX_INT8:
        raise DeserializationError('%r out of range for signed 8-bit integer'
                                   % (x))
    return x


def deserialize_int16(x):
    """Deserialize 16-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to signed 16-bit '
                                   'integer' % (x))
    if x < MIN_INT16 or x > MAX_INT16:
        raise DeserializationError('%r out of range for signed 16-bit integer'
                                   % (x))
    return x


def deserialize_int32(x):
    """Deserialize 32-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to signed 32-bit '
                                   'integer' % (x))
    if x < MIN_INT32 or x > MAX_INT32:
        raise DeserializationError('%r out of range for signed 32-bit integer'
                                   % (x))
    return x


def deserialize_int64(x):
    """Deserialize 64-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to signed 64-bit '
                                   'integer' % (x))
    if x < MIN_INT64 or x > MAX_INT64:
        raise DeserializationError('%r out of range for signed 64-bit integer'
                                   % (x))
    return x


def deserialize_uint8(x):
    """Deserialize 8-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to unsigned 8-bit '
                                   'integer' % (x))
    if x < 0 or x > MAX_UINT8:
        raise DeserializationError('%r out of range for unsigned 8-bit '
                                   'integer' % (x))
    return x


def deserialize_uint16(x):
    """Deserialize 16-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to unsigned 16-bit '
                                   'integer' % (x))
    if x < 0 or x > MAX_UINT16:
        raise DeserializationError('%r out of range for unsigned 16-bit '
                                   'integer' % (x))
    return x


def deserialize_uint32(x):
    """Deserialize 32-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to unsigned 32-bit '
                                   'integer' % (x))
    if x < 0 or x > MAX_UINT32:
        raise DeserializationError('%r out of range for unsigned 32-bit '
                                   'integer' % (x))
    return x


def deserialize_uint64(x):
    """Deserialize 64-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise DeserializationError('cannot deserialize %r to unsigned 64-bit '
                                   'integer' % (x))
    if x < 0 or x > MAX_UINT64:
        raise DeserializationError('%r out of range for unsigned 64-bit '
                                   'integer' % (x))
    return x


def deserialize_string(x):
    """Deserialize string.
    """

    if not isinstance(x, (str, unicode)):
        raise DeserializationError('cannot deserialize %r to string' % (x))
    return x


def deserialize_binary(x):
    """Deserialize binary.
    """

    if not isinstance(x, (str, unicode)):
        raise DeserializationError('cannot deserialize %r to binary' % (x))
    return x


def deserialize_bool(x):
    """Deserialize binary.
    """

    if not isinstance(x, bool):
        raise DeserializationError('cannot deserialize %r to boolean' % (x))
    return x


def deserialize_float32(x):
    """Deserialize 32-bit floating point number.
    """

    if not isinstance(x, float):
        raise DeserializationError('cannot deserialize %r to 32-bit floating '
                                   'point number' % (x))
    return x


def deserialize_float64(x):
    """Deserialize 64-bit floating point number.
    """

    if not isinstance(x, float):
        raise DeserializationError('cannot deserialize %r to 64-bit floating '
                                   'point number' % (x))
    return x
