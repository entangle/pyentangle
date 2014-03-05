from enum import Enum as BaseEnum
from .packing import pack_int64
from .deserialization import deserialize_int64
from .exceptions import DeserializationError


class Enum(BaseEnum):
    """Enumeration.
    """

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self._value_ >= other._value_
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self._value_ > other._value_
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self._value_ <= other._value_
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self._value_ < other._value_
        return NotImplemented

    def pack(self, stream):
        """Pack.

        :param stream: Stream to pack the type to.
        """

        stream.write(pack_int64(self.value))

    @classmethod
    def deserialize(cls, ser):
        """Deserialize.

        :raises entangle.DeserializationError:
            if the serialized input could not be deserialized.
        """

        int_value = deserialize_int64(ser)
        try:
            return cls(int_value)
        except ValueError:
            raise DeserializationError('%r is not a valid %s value' %
                                       (int_value, cls.__name__))
