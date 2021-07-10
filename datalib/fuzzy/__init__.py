from dictpath import dictpath
from glom import glom

def all_keys(h, match, keys=[]):
    for k, v in h.items():
        if match == k.split("/")[-1]:
            keys.append(k)

        if type(v) is dict:
            all_keys(v, match, keys)

    return keys

class FuzzyObject:
    def __init__(self, json):
        self.json = json
        self.graph = dictpath(json).explore()

    def __getattr__(self, name):
        keys = []
        keys = all_keys(self.graph, name, keys)
        results = []
        for k in keys:
            results.append(self[k])

        return results[0] if len(results) == 1 else results

    def __getitem__(self, key):
        key = key.replace("/", ".")
        return glom(self.json, key)
