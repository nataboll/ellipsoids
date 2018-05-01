# this class generates data: the set of (x,y)'s

import numpy as np

__author__ = 'natasha'


class Data:
    def __init__(self):
        pass

    n = 2
    m = 100
    x = np.array([n, m])


def generate(self):
    x = np.random.randn(self.n, self.m)
    x[:, 50] = 10 * np.random.randn(self.n, 1)
    x[:, 80] = 10 * np.random.randn(self.n, 1)
    x[:, 30] = 10 * np.random.randn(self.n, 1)
