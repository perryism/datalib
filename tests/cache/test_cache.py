import unittest
from datalib import cache
import mock

class TestCache(unittest.TestCase):
    @mock.patch("datalib.cache.Storage")
    @mock.patch("datalib.cache.Stream")
    def test_create_with_cache(self, stream_mock, storage_mock):
        storage_instance = mock.Mock()
        storage_mock.return_value = storage_instance
        stream_instance = mock.Mock()
        stream_mock.return_value = stream_instance

        cache_strategy = cache.create("foo", True)
        self.assertEqual(cache_strategy, stream_instance)

        storage_mock.assert_called_with("foo")
        stream_mock.assert_called_with(storage_instance)

    @mock.patch("datalib.cache.Fake")
    def test_create_with_no_cache(self, fake_mock):
        fake_instance = mock.Mock()
        fake_mock.return_value = fake_instance

        cache_strategy = cache.create("foo", False)
        self.assertEqual(cache_strategy, fake_instance)

        fake_mock.assert_called()
