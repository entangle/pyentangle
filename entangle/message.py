class RequestMessage(object):
    """Request message.
    """

    __slots__ = ('message_id', 'method', 'arguments', 'trace')

    def __init__(self, message_id, method, arguments, trace):
        self.message_id = message_id
        self.method = method
        self.arguments = arguments
        self.trace = trace

    def __repr__(self):
        return '<%s.%s: message ID = %d, method = %r, arguments = %r, ' \
            'trace = %r>' % (self.__class__.__module__,
                             self.__class__.__name__,
                             self.message_id,
                             self.method,
                             self.arguments,
                             self.trace)


class NotificationMessage(object):
    """Notification message.
    """

    __slots__ = ('message_id', 'method', 'arguments')

    def __init__(self, message_id, method, arguments):
        self.message_id = message_id
        self.method = method
        self.arguments = arguments

    def __repr__(self):
        return '<%s.%s: message ID = %d, method = %r, arguments = %r, ' \
            'trace = %r>' % (self.__class__.__module__,
                             self.__class__.__name__,
                             self.message_id,
                             self.method,
                             self.arguments)


class ResponseMessage(object):
    """Response message.
    """

    __slots__ = ('message_id', 'result', 'trace')

    def __init__(self, message_id, result, trace):
        self.message_id = message_id
        self.result = result
        self.trace = trace

    def __repr__(self):
        return '<%s.%s: message ID = %d, result = %r, trace = %r>' \
            (self.__class__.__module__,
             self.__class__.__name__,
             self.message_id,
             self.result,
             self.trace)


class ExceptionMessage(object):
    """Exception message.
    """

    __slots__ = ('message_id', 'definition', 'name', 'description', 'trace')

    def __init__(self, message_id, definition, name, description, trace):
        self.message_id = message_id
        self.definition = definition
        self.name = name
        self.description = description
        self.trace = trace

    def __repr__(self):
        return '<%s.%s: message ID = %d, definition = %r, name = %r, ' \
            'description = %r, trace = %r>' % (self.__class__.__module__,
                                               self.__class__.__name__,
                                               self.message_id,
                                               self.definition,
                                               self.name,
                                               self.description,
                                               self.trace)


class NotificationAcknowledgementMessage(object):
    """Notification acknowledgement message.
    """

    __slots__ = ('message_id')

    def __init__(self, message_id):
        self.message_id = message_id

    def __repr__(self):
        return '<%s.%s: message ID = %d>' % (self.__class__.__module__,
                                             self.__class__.__name__,
                                             self.message_id)
