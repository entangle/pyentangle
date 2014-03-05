import errno
import msgpack
import snappy
import socket
from io import BytesIO
from .deserialization import (
    deserialize_binary,
    deserialize_bool,
    deserialize_string,
    deserialize_uint32,
)
from .exceptions import (
    BadMessageError, DeserializationError, ConnectionLostError,
)
from .message import (
    ExceptionMessage,
    NotificationMessage,
    ResponseMessage,
    RequestMessage,
    NotificationAcknowledgementMessage,
)
from .opcode import Opcode
from .packing import packer
from .trace import Trace


class Connection(object):
    """Entangle connection.
    """

    def __init__(self, sock):
        """Initialize an Entangle connection.

        :param sock: Python socket or object of equivalent interface.
        """

        self._sock = sock
        self._unpacker = msgpack.Unpacker()

    def _send(self, data):
        """Send data over the wire.

        :param data: Data to send.
        """

        while data:
            try:
                sent = self._sock.send(data)
            except socket.error as (code, msg):
                if code == errno.EINTR:
                    continue
                if code == errno.EPIPE:
                    raise ConnectionLostError('connection lost')
                raise

            if sent == 0:
                raise ConnectionLostError('connection lost')

            data = data[sent:]

    def send_request(self, message_id, method, packed_arguments, trace=False):
        """Send request.

        :param message_id: Message ID.
        :param method: Method name.
        :param packed_arguments: Package arguments.
        :param trace: Request trace. Default ``False``.
        """

        # Build the request.
        stream = BytesIO()

        stream.write(packer.pack_array_header(5))
        stream.write(packer.pack(Opcode.request.value))
        stream.write(packer.pack(message_id))
        stream.write(packer.pack(method))
        stream.write(packed_arguments)
        stream.write(packer.pack(trace))

        stream.seek(0)

        # Send the data.
        self._send(stream.getvalue())

    def send_notification(self, message_id, method, packed_arguments):
        """Send notification.

        :param message_id: Message ID.
        :param method: Method name.
        :param packed_arguments: Package arguments.
        """

        # Build the request.
        stream = BytesIO()

        stream.write(packer.pack_array_header(4))
        stream.write(packer.pack(Opcode.notification.value))
        stream.write(packer.pack(message_id))
        stream.write(packer.pack(method))
        stream.write(packed_arguments)

        stream.seek(0)

        # Send the data.
        self._send(stream.getvalue())

    def receive(self):
        """Receive message.
        """

        # Receive the message data.
        while True:
            buf = self._sock.recv(4096)
            if not buf:
                raise ConnectionLostError('connection lost')

            self._unpacker.feed(buf)

            try:
                ser = self._unpacker.unpack()
            except msgpack.OutOfData:
                continue

            break

        # Deserialize the message data.
        return self._deserialize_message(ser)

    def _deserialize_message(self, ser):
        # Deserialize the response.
        if not isinstance(ser, (list, tuple, )) or len(ser) < 2:
            raise BadMessageError('invalid message data received')

        # Deserialize the opcode and message ID.
        try:
            opcode = Opcode(ser[0])
        except ValueError:
            raise BadMessageError('invalid opcode: %r' % (ser[0]))

        try:
            message_id = deserialize_uint32(ser[1])
        except DeserializationError:
            raise BadMessageError('invalid message ID: %r' % (ser[1]))

        # Deserialize the message based on the opcode.
        ser = ser[2:]

        if opcode == Opcode.request:
            if len(ser) != 3:
                raise BadMessageError('invalid message data received')

            try:
                method = deserialize_string(ser[0])
                trace = deserialize_bool(ser[2])
            except DeserializationError:
                raise BadMessageError('invalid message data received')

            arguments = ser[1]

            if not isinstance(arguments, (list, tuple, )):
                raise BadMessageError('invalid message data received')

            return RequestMessage(message_id, method, arguments, trace)

        if opcode == Opcode.notification:
            if len(ser) != 2:
                raise BadMessageError('invalid message data received')

            try:
                method = deserialize_string(ser[0])
            except DeserializationError:
                raise BadMessageError('invalid message data received')

            arguments = ser[1]

            if not isinstance(arguments, (list, tuple, )):
                raise BadMessageError('invalid message data received')

            return NotificationMessage(message_id, method, arguments)

        if opcode == Opcode.response:
            if len(ser) != 2:
                raise BadMessageError('invalid message data received')

            result = ser[0]
            trace = None

            if ser[1] is not None:
                try:
                    trace = Trace.deserialize(ser[1])
                except DeserializationError:
                    raise BadMessageError('invalid message data received')

            return ResponseMessage(message_id, result, trace)

        if opcode == Opcode.notification_acknowledgement:
            if len(ser) != 0:
                raise BadMessageError('invalid message data received')

            return NotificationAcknowledgementMessage(message_id)

        if opcode == Opcode.exception:
            if len(ser) != 4:
                raise BadMessageError('invalid message data received')

            trace = None

            try:
                definition = deserialize_string(ser[0])
                name = deserialize_string(ser[1])
                description = deserialize_string(ser[2])
                if ser[3] is not None:
                    trace = Trace.deserialize(ser[3])
            except DeserializationError:
                raise BadMessageError('invalid message data received')

            return ExceptionMessage(message_id,
                                    definition,
                                    name,
                                    description,
                                    trace)

        if opcode == Opcode.compressed_message:
            if len(ser) != 2:
                raise BadMessageError('invalid message data received')

            # Determine the compression method and deserialize the data.
            try:
                method = Opcode(ser[0])
            except ValueError:
                raise BadMessageError('invalid compression method: %r' %
                                      (ser[0]))

            try:
                compressed_data = deserialize_binary(ser[1])
            except DeserializationError:
                raise BadMessageError('invalid compressed data received')

            # Decompress the received data -- for now, we know that this is
            # Snappy, so let's be dirty. It's 3 AM after all.
            try:
                data = snappy.uncompress(compressed_data)
            except snappy.UncompressError as e:
                raise BadMessageError('decompression error: %s' % (e))

            return self._deserialize_message(data)

        raise NotImplementedError('opcode not implemented: %r' % (opcode))

    def close(self):
        self._sock.close()
