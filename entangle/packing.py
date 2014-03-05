import msgpack
from .exceptions import PackingError
from .constants import (
    MAX_INT8, MIN_INT8, MAX_INT16, MIN_INT16, MAX_INT32, MIN_INT32, MAX_INT64,
    MIN_INT64, MAX_UINT8, MAX_UINT16, MAX_UINT32, MAX_UINT64,
)


packer = msgpack.Packer()
float_packer = msgpack.Packer(use_single_float=True)


def pack_int8(x):
    """Pack 8-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to signed 8-bit integer' % (x))
    if x < MIN_INT8 or x > MAX_INT8:
        raise PackingError('%r out of range for signed 8-bit integer' % (x))
    return packer.pack(x)


def pack_int16(x):
    """Pack 16-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to signed 16-bit integer' % (x))
    if x < MIN_INT16 or x > MAX_INT16:
        raise PackingError('%r out of range for signed 16-bit integer' % (x))
    return packer.pack(x)


def pack_int32(x):
    """Pack 32-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to signed 32-bit integer' % (x))
    if x < MIN_INT32 or x > MAX_INT32:
        raise PackingError('%r out of range for signed 32-bit integer' % (x))
    return packer.pack(x)


def pack_int64(x):
    """Pack 64-bit signed integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to signed 64-bit integer' % (x))
    if x < MIN_INT64 or x > MAX_INT64:
        raise PackingError('%r out of range for signed 64-bit integer' % (x))
    return packer.pack(x)


def pack_uint8(x):
    """Pack 8-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to unsigned 8-bit integer' % (x))
    if x < 0 or x > MAX_UINT8:
        raise PackingError('%r out of range for unsigned 8-bit integer' % (x))
    return packer.pack(x)


def pack_uint16(x):
    """Pack 16-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to unsigned 16-bit integer' % (x))
    if x < 0 or x > MAX_UINT16:
        raise PackingError('%r out of range for unsigned 16-bit integer' % (x))
    return packer.pack(x)


def pack_uint32(x):
    """Pack 32-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to unsigned 32-bit integer' % (x))
    if x < 0 or x > MAX_UINT32:
        raise PackingError('%r out of range for unsigned 32-bit integer' % (x))
    return packer.pack(x)


def pack_uint64(x):
    """Pack 64-bit unsigned integer.
    """

    if not isinstance(x, (int, long)):
        raise PackingError('cannot pack %r to unsigned 64-bit integer' % (x))
    if x < 0 or x > MAX_UINT64:
        raise PackingError('%r out of range for unsigned 64-bit integer' % (x))
    return packer.pack(x)


def pack_string(x):
    """Pack string.
    """

    if not isinstance(x, (str, unicode)):
        raise PackingError('cannot pack %r to string' % (x))
    return packer.pack(x)


def pack_binary(x):
    """Pack binary.
    """

    if not isinstance(x, (str, unicode)):
        raise PackingError('cannot pack %r to binary' % (x))
    return packer.pack(x)


def pack_bool(x):
    """Pack binary.
    """

    if not isinstance(x, bool):
        raise PackingError('cannot pack %r to boolean' % (x))
    return packer.pack(x)


def pack_float32(x):
    """Pack 32-bit floating point number.
    """

    if not isinstance(x, float):
        raise PackingError('cannot pack %r to 32-bit floating point number'
                           % (x))
    return float_packer.pack(x)


def pack_float64(x):
    """Pack 64-bit floating point number.
    """

    if not isinstance(x, float):
        raise PackingError('cannot pack %r to 64-bit floating point number'
                           % (x))
    return packer.pack(x)
