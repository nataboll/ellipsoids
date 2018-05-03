# this class generates data: the set of (x,y)'s

import numpy as np


__author__ = 'natasha'


class Data:
    def __init__(self):
        pass

    n = 2
    m = 100
    x = np.zeros((n, m))    # n strings of m indexes: x and y

    def generate(self):
        self.x = 10 * np.random.randn(self.n, self.m)
        # add a few outliers to the set of points:
        for i in range(2):
            self.x[i, 50] = 100 * np.random.randn()
            self.x[i, 60] = 100 * np.random.randn()
            self.x[i, 80] = 100 * np.random.randn()
            self.x[i, 40] = 100 * np.random.randn()
            self.x[i, 1] = 100 * np.random.randn()
