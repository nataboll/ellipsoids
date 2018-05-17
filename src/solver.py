from src.data import Data
import numpy as np
from scipy.optimize import minimize


# area of ellipse
def f(x):
        return np.pi * (x[0] * x[3] - x[1] * x[2]) ** 2


class Solver:
    def __init__(self, data):
        self.data = data

    # constraint function (x[0] == a, x[1] == b, x[2] == c, x[3] == d, x[4] == alpha, x[5] == beta)
    def h(self, x, number):
        det = x[0] * x[3] - x[1] * x[2]
        if det == 0:
            return 1  # 1 is more than 0 so the constraint does not hold
        else:
            return (1 / det ** 2) * ((x[3] * self.data.df.iloc[0, number] - x[1] * (self.data.df.iloc[1, number]
                                                                                    - x[4] * (det ** 2))) ** 2
                                     + (x[0] * self.data.df.iloc[1, number] - x[2] * self.data.df.iloc[0, number]
                                        - x[5] * (det ** 2)) ** 2) - 1

    # variables used for finding out whether to discard the point
    point_cost = 10
    square_cost = 1  # cost of one m^2 of area
    square = 0.0  # ellipse area - target function value
    a = 0.0  # elements of S
    b = 0.0
    c = 0.0
    d = 0.0
    alpha = 0.0  # shift vector
    beta = 0.0

    data = Data()  # Data object will be transferred here

    def set_fields(self, a, b, c, d, alpha, beta):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.alpha = alpha
        self.beta = beta

    def restrictions(self):  # counting all restrictions and assembling together
        cons = list()  # list of dictionaries
        h_list = list()  # list of constraints - functions h_i

        # number of restrictions == number of points left (columns in new_df)
        for i in range(len(self.data.new_df.columns)):
            h_list.append(lambda x: self.h(x, i))
            cons.append({'type': 'ineq', 'fun': h_list[i]})  # appending each constraint as a dictionary
        return cons

    def optimize(self):  # computing matrix S and vector (alpha, beta)^T
        w = self.minimal_result()
        self.set_fields(w[0], w[1], w[2], w[3], w[4], w[5])
        current_square = f(w[0:4])  # latest calculated square
        print("\n" + "Starting square is " + str(current_square))
        self.data.discard_point(False)

        while True:

            self.square = current_square
            w = self.minimal_result()
            current_square = f(w[0:4])
            delta_square = self.square - current_square  # area change
            if delta_square * self.square_cost < self.point_cost:
                break
            self.set_fields(w[0], w[1], w[2], w[3], w[4], w[5])
            self.data.discard_point(False)

    # counting optimal values for points in new_df
    def minimal_result(self):
            x0 = [2, 1, 1, 1, self.data.center[0], self.data.center[1]]
            result = minimize(f, x0, constraints=self.restrictions())
            return result.x

