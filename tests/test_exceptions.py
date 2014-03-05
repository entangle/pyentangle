from unittest import TestCase
from entangle.exceptions import (
    parse_exception,
    BadMessageError,
    InternalServerError,
    UnknownMethodError,
    InvalidArgumentError,
    UnknownException,
)


class ParseExceptionTestCase(TestCase):
    """Test case for :meth:`parse_exception`.
    """

    def test_parse_exception(self):
        """parse_exception(..)
        """

        for definition, name, expected_cls in [
                ('entangle', 'BadMessage', BadMessageError),
                ('entangle', 'InternalServerError', InternalServerError),
                ('entangle', 'UnknownMethod', UnknownMethodError),
                ('entangle', 'InvalidArgument', InvalidArgumentError),
                ('entangle', 'Horse', UnknownException),
                ('horse', 'Horse', UnknownException),
        ]:
            exc = parse_exception(definition, name, 'Message')
            self.assertIsInstance(exc, expected_cls)
            self.assertEqual(exc.name, name)
            self.assertEqual(exc.definition, definition)
            self.assertEqual(str(exc), 'Message')
