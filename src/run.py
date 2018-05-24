from datetime import datetime

from src.solver import *

startTime = datetime.now()
data = Data()
data.generate()

solver = Solver(data)

print("Initial guess: ", solver.initial_guess)
print("Target function (area) at initial guess: ", f(solver.initial_guess[0:4]))

result = minimize(f, solver.initial_guess)

solver.optimize()

print("Resulting target function (area) without constraints: ", f(result.x[0:4]))
print("Resulting target function (area): ", f(solver.vector[0:4]))
print("Resulting matrix S is: ", solver.vector[0:4])
print("Resulting center of ellipse is: ", solver.vector[4:])
print("Constraints at the end: \n")
for i in range(len(solver.data.new_df.columns)):
    print(solver.h(solver.vector, i))

solver.display()

# # display 'a' rows and 'b' columns of DataFrame
# a = len(data.df.index)
# b = len(data.df.columns)

# with pd.option_context('display.max_rows', a, 'display.max_columns', b):
#    print(data.df)
#    print(data.prev_df)

print("\nExecution time: ", datetime.now() - startTime)
