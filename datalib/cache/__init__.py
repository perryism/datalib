from .strategies.stream import *
from .storage import Storage, CacheFolderNotFound

def create(key, cache=True):
    if cache:
        return Stream(Storage(key))
    else:
        return Fake()
