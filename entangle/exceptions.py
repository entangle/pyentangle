class EntangleException(Exception):
    """Entangle exception.

    All non-system exceptions raised by Entangle and Entangle definitions must
    inherit from :class:`EntangleException`.

    :cvar definition: Definition.
    :cvar name: Name.
    """

    pass


class BadMessageError(EntangleException):
    """Bad message.
    """

    definition = 'entangle'
    name = 'BadMessage'


class InternalServerError(EntangleException):
    """Internal server error.
    """

    definition = 'entangle'
    name = 'InternalServerError'


class UnknownMethodError(EntangleException):
    """Unknown method.
    """

    definition = 'entangle'
    name = 'UnknownMethod'


class InvalidArgumentError(EntangleException):
    """Invalid argument.
    """

    definition = 'entangle'
    name = 'InvalidArgument'


class UnknownException(EntangleException):
    """Unknown exception.
    """

    def __init__(self, definition, name, message):
        super(EntangleException, self).__init__(message)
        self.definition = definition
        self.name = name


class PackingError(EntangleException):
    """Packing error.
    """

    definition = 'entangle'
    name = 'PackingError'


class DeserializationError(EntangleException):
    """Deserialization error.
    """

    definition = 'entangle'
    name = 'DeserializationError'


class UnexpectedMessageError(EntangleException):
    """Unexpected message.
    """

    definition = 'entangle'
    name = 'UnexpectedMessage'


class ConnectionLostError(EntangleException):
    """Connection lost.
    """

    definition = 'entangle'
    name = 'ConnectionLost'


entangle_exceptions = {
    BadMessageError.name: BadMessageError,
    InternalServerError.name: InternalServerError,
    UnknownMethodError.name: UnknownMethodError,
    InvalidArgumentError.name: InvalidArgumentError,
}
"""Entangle exceptions.
"""


def parse_exception(definition, name, message):
    """Parse an exception.

    :param definition: Definition.
    :param name: Name.
    :param message: Message.
    :returns:
        the parsed exception or :class:`UnknownException` if the exception is
        not known.
    """

    if definition == 'entangle':
        try:
            return entangle_exceptions[name](message)
        except KeyError:
            pass

    return UnknownException(definition, name, message)
