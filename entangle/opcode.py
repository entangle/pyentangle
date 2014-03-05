from enum import Enum


class Opcode(Enum):
    """Opcode.
    """

    request = 0
    """Request opcode.
    """

    notification = 1
    """Notification opcode.
    """

    response = 2
    """Response opcode.
    """

    exception = 3
    """Exception opcode.
    """

    notification_acknowledgement = 4
    """Notification acknowledgement opcode.
    """

    compressed_message = 0x7f
    """Compressed message opcode.
    """
