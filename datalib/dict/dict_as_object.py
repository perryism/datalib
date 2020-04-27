class DictAsObject:
    def __init__(self, dic):
        self._dict = dic

    def __getattr__(self, name):
        if name == "value":
            return self._dict

        v = self._dict[name]
        return DictAsObject(v)
