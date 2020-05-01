import logging
import os

logger = logging.getLogger(__name__)

class CacheFolderNotFound(Exception):
    pass

class Storage:
    def __init__(self, key):
        self.cached_base = os.environ.get("CACHE_PATH", "/tmp/")
        self.cache_path = os.path.join(self.cached_base, key)
        folder = os.path.dirname(self.cache_path)

        if not os.path.isdir(folder):
            raise CacheFolderNotFound(folder)

        self.key = key

    def is_available(self):
        return os.path.isfile(self.cache_path)
