from datetime import datetime

from src.solver import *
from src.goodsolver import *
import numpy as np

# data = Data()
# data.generate()
#
# solver = Solver(data)
#
# print(solver)
#
# # constraints don't satisfied
#
#
# # cons = list()
# h_list = list()
#
# # h_list.append(lambda x: solver.h(x, 0))
# h_list.append(lambda x: -((1 / (x[0] * x[3] - x[1] * x[2]) ** 2) * ((x[3] * solver.data.df.iloc[0, 0]
#                                                                    - x[1] * (solver.data.df.iloc[1, 0]
#                                                                              - x[4] * ((x[0] * x[3]
#                                                                                         - x[1] * x[2]) ** 2))) ** 2
#                                                                   + (x[0] * solver.data.df.iloc[1, 0]
#                                                                      - x[2] * solver.data.df.iloc[0, 0]
#                                                                      - x[5] * ((x[0] * x[3]
#                                                                                 - x[1] * x[2]) ** 2)) ** 2) - 1))
# # h_list.append(lambda x: solver.h(x, 1))
#
# x0 = [1, 0, 0, 1, solver.data.center[0], solver.data.center[1]]

# cons.append({'type': 'ineq', 'fun': h_list[0]})
# cons = ({'type': 'ineq', 'fun': lambda x: -((1 / (x[0] * x[3] - x[1] * x[2]) ** 2) * ((x[3] * solver.data.df.iloc[0, 0]
#                                                                    - x[1] * (solver.data.df.iloc[1, 0]
#                                                                              - x[4] * ((x[0] * x[3]
#                                                                                         - x[1] * x[2]) ** 2))) ** 2
#                                                                   + (x[0] * solver.data.df.iloc[1, 0]
#                                                                      - x[2] * solver.data.df.iloc[0, 0]
#                                                                      - x[5] * ((x[0] * x[3]
#                                                                                 - x[1] * x[2]) ** 2)) ** 2) - 1)})
# # cons = (cons, {'type': 'ineq', 'fun': h_list[1]})
# # print("Dictionary of constraints: ", cons)
#
# # result = minimize(f, x0, constraints=solver.restrictions())
#
# print("Starting point is: ", x0)
# print("Constraint at the beginning: ", h_list[0](x0))
# print("Function before: ", f(x0))
#
# # print(solver.restrictions())
#
# result = minimize(f, x0, method='SLSQP', constraints=solver.restrictions())
# # solver.optimize()
#
# # another_result = solver.a, solver.b, solver.c
# print("Function after: ", f(result.x))
# # print(solver.h(x0, 0))
# print("Resulting point is: ", result.x)
# # print("Optimized point is: ", solver.vector)
# print("Constraint at the end: ", h_list[0](result.x))
# for i in range(len(solver.data.new_df.columns)):
#     print(solver.h(result.x, i))
#
# # solver.display()

startTime = datetime.now()
data = Data()
data.generate()

solver = Solver(data)

print("Initial guess: ", solver.initial_guess)
print("Target function (area) at initial guess: ", f(solver.initial_guess[0:4]))

# check what ellipse is found without constraints
#result = minimize(f, solver.initial_guess)

#solver.optimize()

#print("Resulting target function (area) without constraints: ", f(result.x[0:3]))
#print("Resulting target function (area): ", f(solver.vector[0:3]))
#print("Resulting center of ellipse is: ", solver.vector[3:])
#print("Constraints at the end: \n")
#for i in range(len(solver.data.new_df.columns)):
#    print(solver.h(solver.vector, i))

# solver.display()
solver.optimize()

print("Resulting target function (area): ", f(solver.initial_guess[0:2]))
print("Resulting elements are: ", solver.initial_guess[0:5])
solver.check_constraints(solver.initial_guess)
#print("Resulting center of ellipse is: ", solver.vector[3:])
#print("Constraints at the end: \n")
#for i in range(len(solver.data.new_df.columns)):
#    print(solver.h(solver.vector, i))

#solver.display()

# # display 'a' rows and 'b' columns of DataFrame
# a = len(data.df.index)
# b = len(data.df.columns)

# with pd.option_context('display.max_rows', a, 'display.max_columns', b):
#    print(data.df)
#    print(data.prev_df)

#print("\nExecution time: ", datetime.now() - startTime)
