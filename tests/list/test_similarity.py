from Levenshtein import distance, ratio
import unittest
from datalib.list.similarity import similarity_ratios, similarity_analysis

class TestDistance(unittest.TestCase):
    def test_distance(self):
        l = ["perryism@gmail.com", "perryism", "perryism@yahoo.com", "perryism@gmail.co"]
        ratios = similarity_ratios(l)
        self.assertGreater(ratios[("perryism@gmail.com", "perryism")], 0.6)
        self.assertGreater(ratios[("perryism@gmail.com", "perryism@yahoo.com")], 0.76)

    def test_similar(self):
        l = ["perryism@gmail.com", "perryism", "perryism@yahoo.com", "perryism@gmail.co"]
        result = similarity_analysis(l)
        self.assertGreater(result["similarity"], 0.7)

        l = ["perryism@gmail.com", "perryism@yahoo.com"]
        result = similarity_analysis(l)
        self.assertGreater(result["similarity"], 0.7)

    def test_difference(self):
        l = ["perryism", "peter", "foobar"]
        result = similarity_analysis(l)
        self.assertLess(result["similarity"], 0.3)

        l = ["perryism", "peter"]
        result = similarity_analysis(l)
        self.assertLess(result["similarity"], 0.5)

        l = ["perryism@gmail.com", "foo", "perryism@yahoo.com", "annie"]
        result = similarity_analysis(l)
        self.assertLess(result["similarity"], 0.3)
