import unittest
from datalib.dict import DictAsObject

class TestDictAsObject(unittest.TestCase):
    def setUp(self):
        jsn = { "a": 3, "b": 4, "c": { "d": [ 1, 2, 3] }, "e": [ 4 ] }
        self.jao = DictAsObject(jsn)

    def test_attribute(self):
        self.assertEqual(self.jao.a.value, 3)
        self.assertEqual(self.jao.c.value, { "d": [1,2,3] })
        self.assertEqual(self.jao.c.d.value, [1,2,3])

        with self.assertRaises(KeyError) as context:
           self.jao.z
