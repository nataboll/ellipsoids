# DO NOT FORGET CLEARING "+1" IN count_restriction

from src.data import Data
import numpy as np


# import pandas as pd


def f(a, b, c, d):
    return np.pi * (a * d - b * c) ** 2


def h(a, b, c, d, alpha, beta, x, y):  # counting restriction: it must be \leq 0
    return 1 / np.abs(a * d - b * c + 1) ** 2 * (  # +1 IN "ABS" IS FOR TESTING
            (d * (x - alpha) - b * (y - beta)) ** 2 +
            (a * (y - beta) - c * (x - alpha)) ** 2) - 1


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

    def set_f(self, a, b, c, d):  # computing target function
        self.f = f(a, b, c, d)

    def set_fields(self, a, b, c, d, alpha, beta):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.alpha = alpha
        self.beta = beta

    def set_restrictions(self):  # counting all restrictions and assembling together
        i = 0
        for x in self.data.x[0, :]:
            y = self.data.x[1, i]
            i += 1
            self.restrictions = np.append(self.restrictions,
                                          h(self.a, self.b, self.c, self.d, self.alpha, self.beta, x, y))

    def optimize(self):  # computing matrix S and vector (alpha, beta)^T
        pass
