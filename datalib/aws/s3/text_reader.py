import logging
import boto3, os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from datalib import cache

class TextReader:
    def __init__(self, bucket, key, use_cache=True):
        self.bucket = bucket
        self.key = key
        self.s3 = boto3.client('s3')
        self.stream = cache.create(key, use_cache)

    def read(self):
        with self.stream(self._stream()) as stream:
            for line in stream:
                yield line

    def _stream(self):
        # if you are getting connection not closed warning
        # https://github.com/boto/boto3/issues/454
        obj = self.s3.get_object(Bucket=self.bucket, Key=self.key)
        body = obj['Body']
        return body._raw_stream
