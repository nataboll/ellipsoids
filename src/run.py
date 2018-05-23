from datetime import datetime
import pandas as pd

from src.data import Data
from src.solver import Solver
import numpy as np


startTime = datetime.now()
data = Data()
data.generate()

solver = Solver(data)
# solver.optimize()
solver.set_fields(1, 1, 1, 1, 0, 0)
solver.display()
# print("\n" + "square = " + str(solver.square) + "\n")
# print("a = " "%.3f" % solver.a + "\n")
# print("b = " "%.3f" % solver.b + "\n")
# print("c = " "%.3f" % solver.c + "\n")
# print("d = " "%.3f" % solver.d + "\n")
# print("alpha = " "%.3f" % solver.alpha + "\n")
# print("beta = " "%.3f" % solver.beta + "\n")


# display 'a' rows and 'b' columns of DataFrame
a = len(data.df.index)
b = len(data.df.columns)

# with pd.option_context('display.max_rows', a, 'display.max_columns', b):
#    print(data.df)
#    print(data.prev_df)

# print("\nExecution time: ", datetime.now() - startTime)
