import pandas as pd
import numpy as np


from src.data import Data

data = Data()
data.generate()
data.toDataFrame()

#Display 'a' rows and 'b' columns of dataframe
a = len(data.df.index)
b = len(data.df.columns)
with pd.option_context('display.max_rows', a, 'display.max_columns', b):
    print(data.df)