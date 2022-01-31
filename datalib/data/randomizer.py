from scipy.stats import gamma
from toolz import curry

@curry
def build_gamma(a, m, n):
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gamma.html
    return gamma.rvs(a=a, size=n) * m

from random import randrange
from faker import Faker
class StrategyBuilder:
    @staticmethod
    def build(strategy):
        if type(strategy) is str:
            if strategy == "postcode":
                fake = Faker()
                return lambda n: [ fake.postcode() for _ in range(n) ]
            else:
                raise NotImplementedError
        else:
            if "normal" in strategy.keys():
               m = strategy["normal"]
               return lambda n: [ randrange(m) for _ in range(n) ]
            elif "chance" in strategy.keys():
                fake = Faker()
                ch = strategy["chance"]
                return lambda n: [ fake.boolean(chance_of_getting_true=ch) for _ in range(n) ]
            elif "gamma" in strategy.keys():
                a = strategy["gamma"]["a"]
                m = strategy["gamma"]["m"]
                gamma = build_gamma(a, m)
                return lambda n: gamma(n)
