from datalib.dict import Mapper
import unittest

class TestMapper(unittest.TestCase):
    def test_mapper(self):
        mapping = {
                "name": lambda x: x["Name"].lower(),
                "place": "Location",
                "phone": lambda x: x["tel"].replace("-", "")
                }


        d = { "Name": "Perry", "Location": "Hong Kong", "tel": "123-123-1232" }
        mapper = Mapper(d, mapping)
        self.assertEqual(mapper.name, "perry")
        self.assertEqual(mapper.place, "Hong Kong")
        self.assertEqual(mapper.phone, "1231231232")
