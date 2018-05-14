from datetime import datetime
import pandas as pd

from scipy.optimize import minimize

from src.data import Data
from src.solver import Solver
import numpy as np


startTime = datetime.now()
data = Data()
data.generate()

# print("\nExecution time: ", datetime.now() - startTime)

# solver = Solver(data)
# solver.optimize(10, 10)   # parameters are needed to be found somehow
# print(solver.w)
# print(solver.mu)

# solver.set_q_value()
# print(solver.q_value)


# constraint function
def h(x, number):
    if (x[0] * x[3] - x[1] * x[2]) == 0:
        return 1  # 1 is more than 0 so the constraint does not hold
    else:
        return 1 / (x[0] * x[3] - x[1] * x[2]) ** 2 * (
                    (x[3] * (data.df.iloc[0, number] - x[4]) - x[1] * (data.df.iloc[1, number] - x[5])) ** 2 +
                    (x[0] * (data.df.iloc[1, number] - x[5]) - x[2] * (data.df.iloc[0, number] - x[4])) ** 2) - 1


# area of ellipse
def f(x):
    return np.pi * (x[0] * x[3] - x[1] * x[2]) ** 2


cons = list()  # list of dictionaries
h_list = list()  # list of constraints

for i in range(data.m):
    h_list.append(lambda x: h(x, i))
    cons.append({'type': 'ineq', 'fun': h_list[i]})  # appending each constraint as a dictionary

x0 = [2, 1, 1, 1, data.center[0], data.center[1]]

# print(cons)

# print(data.center)

for i in range(97):
    data.discard_point(False)
# data.discard_point()
# print(data.df)

print(data.center)

result = minimize(f, x0, constraints=cons)

print(result.x)
print(result)

# display 'a' rows and 'b' columns of DataFrame
a = len(data.df.index)
b = len(data.df.columns)

with pd.option_context('display.max_rows', a, 'display.max_columns', b):
#    print(data.df)
    print(data.new_df)
# print(data.new_df.iloc[0, 1])
