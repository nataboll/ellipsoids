# DO NOT FORGET CLEARING "+1" IN count_restriction

from src.data import Data
import numpy as np
# import pandas as pd


class Solver:
    def __init__(self, data):
        self.data = data

    a = 0.0  # elements of S
    b = 0.0
    c = 0.0
    d = 0.0
    alpha = 0.0  # shift vector
    beta = 0.0
    f = 0.0  # target function value
    data = Data()  # Data object will be transferred here
    restrictions = np.array([])  # restrictions array

    def count_f(self):  # computing target function
        self.f = np.pi * (self.a * self.d - self.b * self.c) ** 2

    def count_restriction(self, x, y):  # counting restriction: it must be \leq 1
        return 1 / np.abs(self.a * self.d - self.b * self.c + 1) * (   # +1 IN "ABS" IS FOR TESTING
                (self.d * (x - self.alpha) - self.b * (y - self.beta)) ** 2 +
                (self.a * (y - self.beta) - self.c * (x - self.alpha)) ** 2)

    def form_restrictions(self):  # counting all restrictions and assembling together
        i = 0
        for x in self.data.x[0, :]:
            y = self.data.x[1, i]
            i += 1
            self.restrictions = np.append(self.restrictions, self.count_restriction(x, y))

    def optimize(self):  # computing matrix S and vector (alpha, beta)^T
        pass
