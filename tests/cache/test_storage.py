import unittest
import mock
import tempfile
import os
from mock import patch
from datalib.cache import Storage, CacheFolderNotFound
from pathlib import Path

class TestStorage(unittest.TestCase):
    @patch("datalib.cache.storage.os.environ")
    def test_invalid_folder(self, environ_mock):
        environ_mock.get.return_value = "/randompath"

        with self.assertRaises(CacheFolderNotFound):
            storage = Storage("foo")

    @patch("datalib.cache.storage.os.environ")
    def test_file(self, environ_mock):
        with tempfile.TemporaryDirectory() as tmp:
            environ_mock.get.return_value = tmp

            storage = Storage("foo")
            self.assertEqual(storage.is_available(), False)

            Path(os.path.join(tmp, "foo")).touch()
            self.assertEqual(storage.is_available(), True)
