import unittest
import mock
from datalib.cache.strategies import *
import tempfile
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

class TestStream(unittest.TestCase):
    def test_fake(self):
        with Fake()("foo") as f:
            self.assertEqual(f, "foo")

    def test_no_cache_stream(self):
        storage = mock.Mock()
        storage.is_available.return_value = False

        with tempfile.TemporaryDirectory() as tmp:
            storage.cache_path = os.path.join(tmp, "foo.txt")

            cache = Stream(storage, "w")

            with open("tests/fixtures/dummy.txt") as stream:
                with cache(stream) as f:
                    pass

            with open(storage.cache_path) as f:
                self.assertEqual(f.readline(), "line 1\n")
                self.assertEqual(f.readline(), "line 2\n")
                self.assertEqual(f.readline(), "line 3\n")
