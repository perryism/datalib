import unittest
from datalib.performance import timer
import mock
from datetime import datetime

class TestTimer(unittest.TestCase):
    @mock.patch("datalib.performance.logging")
    @mock.patch("datalib.performance.datetime")
    def test_timer(self, datetime_mock, logging_mock):
        logger = mock.Mock()
        logging_mock.getLogger.return_value = logger
        datetime_mock.now.side_effect = [ datetime(2015, 3, 26, 0, 0, 0), datetime(2015, 3, 26, 0, 1, 0)]

        @timer("foo")
        def foo():
            return "bar"
        #it doesn't change the original funcationality
        self.assertEqual(foo(), "bar")
        logging_mock.getLogger.assert_called_with("timer")
        logger.debug.assert_called_with("foo 0:01:00")
