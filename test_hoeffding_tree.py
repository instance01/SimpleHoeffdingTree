import unittest
import math
from hoeffding_tree import HoeffdingTree


class TestHoeffdingTree(unittest.TestCase):
    def test1(self):
        Nmin = 2
        delta = 0.2
        R = 1
        logfunc = math.log2
        tree = HoeffdingTree(Nmin, delta, R, logfunc)
        data_columns = {
            'time': ['1-2', '2-7', '>7', '1-2', '>7', '1-2', '2-7', '2-7'],
            'gender': ['m', 'm', 'f', 'f', 'm', 'm', 'f', 'm'],
            'area': ['urban', 'rural', 'rural', 'rural', 'rural', 'rural', 'urban', 'urban']
        }
        label_columns = [
            ['low', 'high', 'low', 'high', 'high', 'high', 'low', 'low']
        ]
        tree.fit(data_columns, label_columns[0])

    def test2(self):
        Nmin = 2
        delta = 0.2
        R = 1
        logfunc = math.log2
        tree = HoeffdingTree(Nmin, delta, R, logfunc)
        data_columns = {
            'ab': ['a', 'b', 'b', 'b', 'a', 'a', 'b', 'b'],
            '012': [2, 1, 0, 1, 1, 0, 1, 2],
            'm1m2': ['m1', 'm2', 'm1', 'm2', 'm2', 'm1', 'm2', 'm1']
        }
        label_columns = [
            [0, 0, 1, 1, 0, 0, 1, 1]
        ]
        tree.fit(data_columns, label_columns[0])

    def test3(self):
        Nmin = 2
        delta = 0.2
        R = 1
        logfunc = math.log2
        tree = HoeffdingTree(Nmin, delta, R, logfunc)
        data_columns = {
            'ab': ['a', 'b', 'b', 'b', 'a', 'a', 'b', 'b'],
            '012': [2, 1, 0, 1, 1, 2, 1, 0],
            'm1m2': ['m1', 'm2', 'm1', 'm2', 'm2', 'm1', 'm2', 'm1']
        }
        label_columns = [
            [0, 0, 1, 1, 0, 0, 1, 1]
        ]
        tree.fit(data_columns, label_columns[0])


if __name__ == '__main__':
    unittest.main()
