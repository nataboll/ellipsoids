from src.data import Data
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# area of ellipse
def f(x):
    return 1 / (x[0] ** 4 * x[1] ** 4)


def gradf(x):
    res = np.zeros(5)
    res[0] = - 4 / (x[0]**5 * x[1]**4)
    res[1] = - 4 / (x[0]**4 * x[1]**5)
    return res


class Solver:
    def __init__(self, data):
        self.data = data

    data = Data()
    x = 0
    y = 0
    z = 0
    alpha = 0
    beta = 0
    square = 0
    vector = np.zeros(5)
    initial_guess = np.array([0.1, 0.1, 0, data.center[0], data.center[1]])

    def set_fields(self, x, y, z, alpha, beta):
        self.x = x
        self.y = y
        self.z = z
        self.alpha = alpha
        self.beta = beta
        self.vector = [x, y, z, alpha, beta]
        self.square = f(self.vector)

    # constraints
    # x[0] == x, x[1] == y, x[2] == z, x[3] == alpha, x[4] == beta

    def h(self, x, number):
        return (x[0] ** 2 * self.data.df.iloc[0, number] + x[0] * x[2] * self.data.df.iloc[1, number] - x[3]) ** 2 +\
               (x[0] * x[2] * self.data.df.iloc[0, number] + (x[1] ** 2 + x[2] ** 2) * self.data.df.iloc[1, number]
                - x[4]) ** 2 - 1

    def gradh(self, x, number):
        x_i = self.data.df.iloc[0, number]
        y_i = self.data.df.iloc[1, number]
        res = np.zeros(5)
        # x[3] * x_i --> x[2] * x_i in the end
        res[0] = 2 * (x[0]**2 * x_i + x[0] * x[2] * y_i - x[3]) * ( 2 * x[0] * x_i + x[2] * y_i) + 2 *\
                 (x[0] * x[2] * x_i + (x[1]**2 + x[2]**2) * y_i - x[4]) * x[2] * x_i
        res[1] = 2 * (x[0] * x[2] * x_i + (x[1]**2 + x[2]**2) * y_i - x[4]) * 2 * y_i * x[1]
        res[2] = 2 * (x[0]**2 * x_i + x[0] * x[2] * y_i - x[3]) * x[0] * y_i + 2 *\
                 (x[0] * x[2] * x_i + (x[1]**2 + x[2]**2) * y_i - x[4]) * (x[0] * x_i + 2 * x[2] * y_i)
        res[3] = - 2 * (x[0]**2 * x_i + x[0] * x[2] * y_i - x[3])
        res[4] = - 2 * (x[0] * x[2] * x_i + (x[1]**2 + x[2]**2) * y_i - x[4])
        return res

    def q(self, x, t):
        return f(x) - t*np.log(- self.h(x, 0)) - t*np.log(- self.h(x, 10)) - t*np.log(- self.h(x, 20))

    def gradq(self, x, t):
        return gradf(x) - t * self.gradh(x, 0) / self.h(x, 0) + t * self.gradh(x, 10) / self.h(x, 10) -\
                                t * self.gradh(x, 20) / self.h(x, 20)

    def hessq(self, x, t):
        return np.identity(5)

    def super_minimize(self):
        gamma = 0.9
        t = 1
        epsilon = 10**(-7)
        while t*self.data.m > epsilon:
            q = lambda x: self.q(x, t)
            gradq = lambda x: self.gradq(x, t)
            hessq = lambda x: self.hessq(x, t)
            #result = minimize(q, self.initial_guess, jac=gradq, method='CG')
            #self.initial_guess = result.x
            print("NEW T = ", t, ", x = ", self.initial_guess, ", q = ", q(self.initial_guess))
            print("now h equals: ", self.h(self.initial_guess, 0), self.h(self.initial_guess, 10), self.h(self.initial_guess, 20))
            #self.initial_guess = self.newton(self.initial_guess, t, epsilon, 100)
            self.initial_guess = self.gradient_descent(self.initial_guess, gradq, epsilon)
            t = gamma * t
        return self.initial_guess

    def gradient_descent(self, x0, gradff, epsilon):
        x = x0
        iteration = 0
        while np.linalg.norm(gradff(x)) > epsilon:
            h = gradff(x)
            alpha = 0.8
            x = x - alpha * h
            iteration += 1
            #print(x, iteration)
        return x

    def newton(self, x0, t, epsilon, num_iter, **kwargs):
        x = x0
        iteration = 0
        q = lambda x: self.q(x, t)
        gradq = lambda x: self.gradq(x, t)
        hessq = lambda x: self.hessq(x, t)
        opt_arg = {"q": q, "grad_q": gradq}
        for key in kwargs:
            opt_arg[key] = kwargs[key]
        while True:
            gradient = gradq(x)
            hess = hessq(x)
            h = -np.linalg.solve(hess, gradient)
            alpha = 1
            x = x + alpha * h
            iteration += 1
            print(x, iteration)
            if np.linalg.norm(gradq(x)) < epsilon:
                break
            if iteration >= num_iter:
                break
        return x
