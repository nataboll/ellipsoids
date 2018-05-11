# DO NOT FORGET CLEARING "+1" IN count_restriction

from src.data import Data
import numpy as np


# import pandas as pd


def f(a, b, c, d):
    return np.pi * (a * d - b * c) ** 2


def grad_f(a, b, c, d):
    return 2 * np.pi * (a * d - b * c) * [d, -c, -b, a]


def h(a, b, c, d, alpha, beta, x, y):  # counting restriction: it must be \leq 0
    return 1 / (a * d - b * c + 1) ** 2 * (  # +1 IN "ABS" IS FOR TESTING
            (d * (x - alpha) - b * (y - beta)) ** 2 +
            (a * (y - beta) - c * (x - alpha)) ** 2) - 1


def grad_h(a, b, c, d, alpha, beta, x, y):  # change later if needed
    return [a, b, c, d, alpha, beta]


class Solver:
    def __init__(self, data):
        self.data = data

    a = 0.0  # elements of S
    b = 0.0
    c = 0.0
    d = 0.0
    alpha = 0.0  # shift vector
    beta = 0.0
    mu = 1.0
    w = np.array([a, b, c, d, alpha, beta])
    f_value = 0.0  # target function value
    q_value = 0.0
    data = Data()  # Data object will be transferred here
    restrictions = np.array([])  # restrictions array
    tol = 1   # barrier parameter

    def q(self, a, b, c, d, alpha, beta, mu):
        sum_h = np.sum(h(a, b, c, d, alpha, beta, self.data.x[0, :], self.data.x[1, :]))
        return f(a, b, c, d) + mu / 2 * sum_h

    def grad_q(self, a, b, c, d, alpha, beta, mu):
        return grad_f(a, b, c, d) + mu / 2 * np.sum(grad_h(a, b, c, d, alpha,
                                                           beta, self.data.x[0, :], self.data.x[1, :]))

    def set_f_value(self):  # computing target function
        self.f_value = f(self.a, self.b, self.c, self.d)

    def set_q_value(self):
        self.q_value = self.q(self.a, self.b, self.c, self.d, self.alpha, self.beta, self.mu)

    def set_fields(self, a, b, c, d, alpha, beta):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.alpha = alpha
        self.beta = beta
        self.w = [self.a, self.b, self.c, self.d, self.alpha, self.beta]

    def set_restrictions(self):  # counting all restrictions and assembling together
        i = 0
        for x in self.data.x[0, :]:
            y = self.data.x[1, i]
            i += 1
            self.restrictions = np.append(self.restrictions,
                                          h(self.a, self.b, self.c, self.d, self.alpha, self.beta, x, y))

    def optimize(self, tol, eps):  # computing matrix S and vector (alpha, beta)^T
        a, b, c, d = 1, 0, 0, 1
        alpha, beta = 1, 1  # will be changed
        mu = 1
        w = np.array([a, b, c, d, alpha, beta])   # starting point
#        Q = q(a, b, c, d, alpha, beta, mu)
#        grad_Q = grad_q(a, b, c, d, alpha, beta, mu)
        while True:
            w = self.minimize_q(w)
            w_norm = np.dot(w, w)
            if tol * w_norm > eps:
                break
            mu *= 15
            self.mu = mu
#            Q = q(a, b, c, d, alpha, beta, mu)
#            grad_Q = grad_q(a, b, c, d, alpha, beta, mu)
        self.set_fields(w[0], w[1], w[2], w[3], w[4], w[5])

    def minimize_q(self, w):   # -> scipy.optimize.minimize()
        return [1, 1, 1, 1, 1, 1]
