import unittest
from datalib.list import intercept

class TestList(unittest.TestCase):
    def test_intercept(self):
        list_one = ["apple", "water"]
        list_two = ["apple", "orange", "banana", "pineapple", "watermelon"]

        self.assertEqual(intercept(list_one, list_two, False), [ "orange", "banana" ])
        self.assertEqual(intercept(list_one, list_two, True), [ "apple", "pineapple", "watermelon" ])
