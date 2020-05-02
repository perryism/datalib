from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)

class Fake:
    @contextmanager
    def __call__(self, stream):
        yield stream

class Stream:
    def __init__(self, storage, mode="wb"):
        self.storage = storage
        self.cache_path = storage.cache_path
        self.mode = mode

    @contextmanager
    def __call__(self, stream):
        if self.storage.is_available():
            logger.info("Cache is found at %s"%self.cache_path)
            with open(self.cache_path, "r") as f:
                yield f
        else:
            logger.info("Cache is not found")

            #TODO: read the stream while writing it down
            with open(self.cache_path, self.mode) as f:
                for line in stream:
                    f.write(line)

            with open(self.cache_path, "r") as f:
                yield f
