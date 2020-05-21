class Mapper(object):
    def __init__(self, d, mapping):
        self.dict = d
        self.mapping = mapping

    def __getattr__(self, name):
        value = self.mapping[name]
        if callable(value):
            return value(self.dict)
        else:
            return self.dict[value]
