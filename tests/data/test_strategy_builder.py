import unittest
from unittest import mock

from datalib.data import randomizer
class TestStrategyBuilder(unittest.TestCase):
    def setUp(self):
        self.subject = randomizer.StrategyBuilder.build

    @mock.patch("datalib.data.randomizer.Faker")
    def testPostCode(self, faker_mock):
        f = mock.Mock()
        faker_mock.return_value = f
        f.postcode.return_value = "123456"

        p = self.subject("postcode")
        zipcodes = p(10)
        self.assertEqual(f.postcode.call_count, 10)
        self.assertEqual(['123456']*10, zipcodes)


    @mock.patch("datalib.data.randomizer.Faker")
    def testChance(self, faker_mock):
        f = mock.Mock()
        faker_mock.return_value = f
        f.boolean.return_value = [False, True, False, True, False, True, False, True, False, True]

        p = self.subject({"chance": 50})
        results = p(10)
        f.boolean.assert_called_with(chance_of_getting_true=50)


    #@mock.patch("datalib.data.randomizer.randrange")
    #def testNormal(self, randrange_mock):
    def testNormal(self):
        p = self.subject({"normal": 50})
        n_samples = 1000
        values = p(n_samples)
        avg = sum(values)/n_samples
        #TODO: would unittest be enough?
        self.assertTrue(23 < avg < 27)

    def testGamma(self):
        from statistics import median
        n_samples = 100
        p = self.subject({"gamma": {"a": 1.99, "m": 1}})
        values = p(n_samples)
        avg = sum(values)/n_samples
        self.assertTrue(1.8 < avg < 2.1)
        is_skewed = median(values) < avg
        self.assertTrue(is_skewed)
