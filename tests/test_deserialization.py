from unittest import TestCase
from entangle.constants import (
    MAX_INT8, MIN_INT8, MAX_INT16, MIN_INT16, MAX_INT32, MIN_INT32, MAX_INT64,
    MIN_INT64, MAX_UINT8, MAX_UINT16, MAX_UINT32, MAX_UINT64,
)
from entangle.deserialization import (
    deserialize_int8,
    deserialize_uint8,
    deserialize_int16,
    deserialize_uint16,
    deserialize_int32,
    deserialize_uint32,
    deserialize_int64,
    deserialize_uint64,
    deserialize_string,
    deserialize_binary,
    deserialize_bool,
    deserialize_float32,
    deserialize_float64,
)
from entangle.exceptions import DeserializationError


class DeserializeInt8TestCase(TestCase):
    """Test case for :meth:`deserialize_int8`.
    """

    def test_deserialize_int8(self):
        """deserialize_int8(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT8, MIN_INT8),
                (MAX_INT8, MAX_INT8),
        ]:
            actual = deserialize_int8(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                MIN_INT8 - 1,
                MAX_INT8 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_int8(ser)


class DeserializeInt16TestCase(TestCase):
    """Test case for :meth:`deserialize_int16`.
    """

    def test_deserialize_int16(self):
        """deserialize_int16(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT16, MIN_INT16),
                (MAX_INT16, MAX_INT16),
        ]:
            actual = deserialize_int16(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                MIN_INT16 - 1,
                MAX_INT16 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_int16(ser)


class DeserializeInt32TestCase(TestCase):
    """Test case for :meth:`deserialize_int32`.
    """

    def test_deserialize_int32(self):
        """deserialize_int32(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT32, MIN_INT32),
                (MAX_INT32, MAX_INT32),
        ]:
            actual = deserialize_int32(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                MIN_INT32 - 1,
                MAX_INT32 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_int32(ser)


class DeserializeInt64TestCase(TestCase):
    """Test case for :meth:`deserialize_int64`.
    """

    def test_deserialize_int64(self):
        """deserialize_int64(..)
        """

        for ser, expected in [
                (0, 0),
                (MIN_INT64, MIN_INT64),
                (MAX_INT64, MAX_INT64),
        ]:
            actual = deserialize_int64(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                MIN_INT64 - 1,
                MAX_INT64 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_int64(ser)


class DeserializeUint8TestCase(TestCase):
    """Test case for :meth:`deserialize_uint8`.
    """

    def test_deserialize_uint8(self):
        """deserialize_uint8(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT8, MAX_UINT8),
        ]:
            actual = deserialize_uint8(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT8 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_uint8(ser)


class DeserializeUint16TestCase(TestCase):
    """Test case for :meth:`deserialize_uint16`.
    """

    def test_deserialize_uint16(self):
        """deserialize_uint16(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT16, MAX_UINT16),
        ]:
            actual = deserialize_uint16(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT16 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_uint16(ser)


class DeserializeUint32TestCase(TestCase):
    """Test case for :meth:`deserialize_uint32`.
    """

    def test_deserialize_uint32(self):
        """deserialize_uint32(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT32, MAX_UINT32),
        ]:
            actual = deserialize_uint32(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT32 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_uint32(ser)


class DeserializeUint64TestCase(TestCase):
    """Test case for :meth:`deserialize_uint64`.
    """

    def test_deserialize_uint64(self):
        """deserialize_uint64(..)
        """

        for ser, expected in [
                (0, 0),
                (MAX_UINT64, MAX_UINT64),
        ]:
            actual = deserialize_uint64(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                -1,
                MAX_UINT64 + 1
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_uint64(ser)


class DeserializeStringTestCase(TestCase):
    """Test case for :meth:`deserialize_string`.
    """

    def test_deserialize_string(self):
        """deserialize_string(..)
        """

        for ser, expected in [
                ('', ''),
                ('  ', '  '),
                (u'', u''),
                (u'  ', u'  '),
                ('String value', 'String value'),
                (u'String value', u'String value'),
        ]:
            actual = deserialize_string(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                1,
                True,
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_string(ser)


class DeserializeBinaryTestCase(TestCase):
    """Test case for :meth:`deserialize_binary`.
    """

    def test_deserialize_binary(self):
        """deserialize_binary(..)
        """

        for ser, expected in [
                ('', ''),
                ('  ', '  '),
                (u'', u''),
                (u'  ', u'  '),
                ('Binary value', 'Binary value'),
                (u'Binary value', u'Binary value'),
        ]:
            actual = deserialize_binary(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                1,
                True,
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_binary(ser)


class DeserializeBoolTestCase(TestCase):
    """Test case for :meth:`deserialize_bool`.
    """

    def test_deserialize_bool(self):
        """deserialize_bool(..)
        """

        for ser, expected in [
                (True, True),
                (False, False),
        ]:
            actual = deserialize_bool(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                1,
                'True',
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_bool(ser)


class DeserializeFloat32TestCase(TestCase):
    """Test case for :meth:`deserialize_float32`.
    """

    def test_deserialize_float32(self):
        """deserialize_float32(..)
        """

        for ser, expected in [
                (0.0, 0.0),
        ]:
            actual = deserialize_float32(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                0,
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_float32(ser)


class DeserializeFloat64TestCase(TestCase):
    """Test case for :meth:`deserialize_float64`.
    """

    def test_deserialize_float64(self):
        """deserialize_float64(..)
        """

        for ser, expected in [
                (0.0, 0.0),
        ]:
            actual = deserialize_float64(ser)
            self.assertEqual(actual, expected)

        for ser in [
                None,
                '1',
                0,
        ]:
            with self.assertRaises(DeserializationError):
                deserialize_float64(ser)
