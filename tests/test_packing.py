import msgpack
from unittest import TestCase
from entangle.constants import (
    MAX_INT8, MIN_INT8, MAX_INT16, MIN_INT16, MAX_INT32, MIN_INT32, MAX_INT64,
    MIN_INT64, MAX_UINT8, MAX_UINT16, MAX_UINT32, MAX_UINT64,
)
from entangle.packing import (
    pack_int8,
    pack_uint8,
    pack_int16,
    pack_uint16,
    pack_int32,
    pack_uint32,
    pack_int64,
    pack_uint64,
    pack_string,
    pack_binary,
    pack_bool,
    pack_float32,
    pack_float64,
)
from entangle.exceptions import PackingError


packer = msgpack.Packer()
float_packer = msgpack.Packer(use_single_float=True)


class PackInt8TestCase(TestCase):
    """Test case for :meth:`pack_int8`.
    """

    def test_pack_int8(self):
        """pack_int8(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT8, MIN_INT8),
                (MAX_INT8, MAX_INT8),
        ]:
            actual = pack_int8(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                MIN_INT8 - 1,
                MAX_INT8 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_int8(ser)


class PackInt16TestCase(TestCase):
    """Test case for :meth:`pack_int16`.
    """

    def test_pack_int16(self):
        """pack_int16(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT16, MIN_INT16),
                (MAX_INT16, MAX_INT16),
        ]:
            actual = pack_int16(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                MIN_INT16 - 1,
                MAX_INT16 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_int16(ser)


class PackInt32TestCase(TestCase):
    """Test case for :meth:`pack_int32`.
    """

    def test_pack_int32(self):
        """pack_int32(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT32, MIN_INT32),
                (MAX_INT32, MAX_INT32),
        ]:
            actual = pack_int32(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                MIN_INT32 - 1,
                MAX_INT32 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_int32(ser)


class PackInt64TestCase(TestCase):
    """Test case for :meth:`pack_int64`.
    """

    def test_pack_int64(self):
        """pack_int64(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT64, MIN_INT64),
                (MAX_INT64, MAX_INT64),
        ]:
            actual = pack_int64(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                MIN_INT64 - 1,
                MAX_INT64 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_int64(ser)


class PackUint8TestCase(TestCase):
    """Test case for :meth:`pack_uint8`.
    """

    def test_pack_uint8(self):
        """pack_uint8(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT8, MAX_UINT8),
        ]:
            actual = pack_uint8(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT8 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_uint8(ser)


class PackUint16TestCase(TestCase):
    """Test case for :meth:`pack_uint16`.
    """

    def test_pack_uint16(self):
        """pack_uint16(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT16, MAX_UINT16),
        ]:
            actual = pack_uint16(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT16 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_uint16(ser)


class PackUint32TestCase(TestCase):
    """Test case for :meth:`pack_uint32`.
    """

    def test_pack_uint32(self):
        """pack_uint32(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT32, MAX_UINT32),
        ]:
            actual = pack_uint32(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT32 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_uint32(ser)


class PackUint64TestCase(TestCase):
    """Test case for :meth:`pack_uint64`.
    """

    def test_pack_uint64(self):
        """pack_uint64(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT64, MAX_UINT64),
        ]:
            actual = pack_uint64(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT64 + 1
        ]:
            with self.assertRaises(PackingError):
                pack_uint64(ser)


class PackStringTestCase(TestCase):
    """Test case for :meth:`pack_string`.
    """

    def test_pack_string(self):
        """pack_string(..)
        """

        for ser, expected in [
                ('', ''),
                ('  ', '  '),
                (u'', u''),
                (u'  ', u'  '),
                ('String value', 'String value'),
                (u'String value', u'String value'),
        ]:
            actual = pack_string(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                1,
                True,
        ]:
            with self.assertRaises(PackingError):
                pack_string(ser)


class PackBinaryTestCase(TestCase):
    """Test case for :meth:`pack_binary`.
    """

    def test_pack_binary(self):
        """pack_binary(..)
        """

        for ser, expected in [
                ('', ''),
                ('  ', '  '),
                (u'', u''),
                (u'  ', u'  '),
                ('Binary value', 'Binary value'),
                (u'Binary value', u'Binary value'),
        ]:
            actual = pack_binary(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                1,
                True,
        ]:
            with self.assertRaises(PackingError):
                pack_binary(ser)


class PackBoolTestCase(TestCase):
    """Test case for :meth:`pack_bool`.
    """

    def test_pack_bool(self):
        """pack_bool(..)
        """

        for ser, expected in [
                (True, True),
                (False, False),
        ]:
            actual = pack_bool(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                1,
                'True',
        ]:
            with self.assertRaises(PackingError):
                pack_bool(ser)


class PackFloat32TestCase(TestCase):
    """Test case for :meth:`pack_float32`.
    """

    def test_pack_float32(self):
        """pack_float32(..)
        """

        for ser, expected in [
                (0.0, 0.0),
        ]:
            actual = pack_float32(ser)
            self.assertEqual(actual, float_packer.pack(expected))

        for ser in [
                None,
                '1',
                0,
        ]:
            with self.assertRaises(PackingError):
                pack_float32(ser)


class PackFloat64TestCase(TestCase):
    """Test case for :meth:`pack_float64`.
    """

    def test_pack_float64(self):
        """pack_float64(..)
        """

        for ser, expected in [
                (0.0, 0.0),
        ]:
            actual = pack_float64(ser)
            self.assertEqual(actual, packer.pack(expected))

        for ser in [
                None,
                '1',
                0,
        ]:
            with self.assertRaises(PackingError):
                pack_float64(ser)
