from datalib.fuzzy import FuzzyObject
import unittest

class TestFuzzyObject(unittest.TestCase):
    def test_me(self):
        j = {
                "foo": {
                    "bar": {
                        "buzz": 123
                    },
                    "buzz": {
                        "bar": 456,
                        "foo": 333
                    }
                }
            }

        fo = FuzzyObject(j)
        self.assertEqual(fo.buzz, [123, {'bar': 456, 'foo': 333}])
        self.assertEqual(fo["foo/buzz/bar"], 456)

