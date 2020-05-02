import unittest
from datalib.aws import s3
import mock
import io

class TestS3TextReader(unittest.TestCase):
    @mock.patch("datalib.aws.s3.text_reader.boto3.client")
    def test_text_read(self, boto_client):
        s3_client = mock.Mock()
        boto_client.return_value = s3_client
        body = mock.Mock()

        with open("tests/fixtures/dummy.txt") as f:
            body._raw_stream = io.StringIO(f.read())

        obj = { "Body": body }
        s3_client.get_object.return_value = obj

        reader = s3.TextReader("foo", "bar", False)
        for i, line in enumerate(reader.read()):
            self.assertEqual(line, "line %d\n"%(i+1))
