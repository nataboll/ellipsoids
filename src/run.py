from datetime import datetime
# import pandas as pd

from src.data import Data
from src.solver import Solver
import numpy as np


startTime = datetime.now()
data = Data()
data.generate()
data.toDataFrame()

# display 'a' rows and 'b' columns of DataFrame
a = len(data.df.index)
b = len(data.df.columns)

# with pd.option_context('display.max_rows', a, 'display.max_columns', b):
#    print(data.df)

# print("\nExecution time: ", datetime.now() - startTime)

solver = Solver(data)
solver.optimize(10, 10)
print(solver.w)
print(solver.mu)

solver.set_q_value()
print(solver.q_value)
