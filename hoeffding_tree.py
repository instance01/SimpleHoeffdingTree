import math
from collections import Counter
from collections import defaultdict


class HoeffdingTree:
    def __init__(self, Nmin, delta, R, logfunc, verbose=True):
        self.Nmin = Nmin
        self.delta = delta
        self.R = R
        self.logfunc = logfunc
        self.verbose = verbose

    def log_debug(self, *msg):
        if self.verbose:
            print(*msg)

    def calc_hoeffding_bound(self, i):
        return (
            (self.R ** 2 * math.log(1. / self.delta)) / (2 * i)
        ) ** .5

    def calc_prior_entropy(self, labels):
        c = Counter(labels)
        entropy = 0
        for label in set(labels):
            p = c[label] / len(labels)
            entropy += p * self.logfunc(p)
        return -entropy

    def calc_total_attr_entropy(self, kv, i):
        self.log_debug(kv.keys())
        weighted_sum = 0
        for item in kv.keys():
            entropy = 0
            count = sum(kv[item].values())
            for label_count in kv[item].values():
                p = label_count / count
                entropy += p * self.logfunc(p)
            weighted_sum += count / i * (-entropy)
            self.log_debug('entropy for', item, ": ", -entropy)
        self.log_debug('weighted_sum:', weighted_sum)
        return weighted_sum

    def fit(self, data_columns, label_column):
        total_len = len(next(iter(data_columns.values())))
        for i in range(1, total_len + 1):
            if i % self.Nmin != 0:
                continue

            self.log_debug(i)

            infogains = []

            for attr_name, col in data_columns.items():
                kv = defaultdict(lambda: defaultdict(int))
                for (item, label) in zip(col[:i], label_column[:i]):
                    kv[item][label] += 1

                prior_entropy = self.calc_prior_entropy(label_column[:i])
                total_attr_entropy = self.calc_total_attr_entropy(kv, i)

                infogain = prior_entropy - total_attr_entropy
                self.log_debug(
                    'infogain:',
                    prior_entropy,
                    "-",
                    total_attr_entropy,
                    '= ',
                    infogain
                )
                infogains.append((infogain, attr_name))

            infogains = sorted(infogains)
            print('All infogains:', infogains)
            eps = self.calc_hoeffding_bound(i)
            if infogains[-1][0] - infogains[-2][0] > eps:
                print('Split on:', infogains[-1][1])
            print('')
