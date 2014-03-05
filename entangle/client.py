import socket
from .constants import MAX_UINT32
from .connection import Connection
from .exceptions import UnexpectedMessageError
from .message import (
    ExceptionMessage,
    ResponseMessage,
)


class Client(object):
    """Client.

    Base class for client implementations. Operates in a non thread safe
    blocking manner.
    """

    def __init__(self,
                 address,
                 connect_timeout=10,
                 reconnect_limit=3):
        """Initialize a client.

        :param address: Address.
        :param connect_timeout: Connect timeout. Default ``10``.
        :param reconnect_limit: Reconnect limit. Default ``3``.
        """

        self._address = address
        self._message_id = 0
        self._connect_timeout = connect_timeout
        self._reconnect_limit = reconnect_limit
        self._conn = None

    def _next_message_id(self):
        """Next message ID.
        """

        self._message_id += 1
        if self._message_id > MAX_UINT32:
            self._message_id = 0
        return self._message_id

    def _get_conn(self):
        """Get connection.
        """

        if self._conn is not None:
            return self._conn

        retry = 0

        while True:
            try:
                sock = socket.create_connection(self._address,
                                                timeout=self._connect_timeout)
                self._conn = Connection(sock)
                return self._conn
            except:
                if retry == self._reconnect_limit:
                    raise

            retry += 1

    def _call(self, name, packed_arguments, trace=False, notify=False):
        """Call a method.

        :param name: Name.
        :param packed_arguments: Package arguments.
        :param trace: Request trace. Ignored if :param:`notify` is ``True``.
        :param notify: Notify instead of request.
        :returns:
            the response message if :param:`notify` is ``False``, otherwise
           ``None`` indicating that the notification has been sent.
        """

        # Get a new message ID.
        message_id = self._next_message_id()

        # Get a connection.
        conn = self._get_conn()

        try:
            # Send the request.
            if notify:
                conn.send_notification(message_id, name, packed_arguments)
            else:
                conn.send_request(message_id, name, packed_arguments, trace)

            # Wait for a response.
            if notify:
                return

            response = conn.receive()
        except:
            # Reset the connection and re-raise.
            self._conn.close()
            self._conn = None
            raise

        # Make sure the response is either a result or an exception.
        if not isinstance(response, (ExceptionMessage, ResponseMessage, )):
            raise UnexpectedMessageError('unexpected response: %r' %
                                         (response))

        # Make sure the message IDs match.
        if response.message_id != message_id:
            raise UnexpectedMessageError(
                'expected response to have message ID %d, but it has message '
                'ID %d' % (message_id, response.message_id)
            )

        return response
