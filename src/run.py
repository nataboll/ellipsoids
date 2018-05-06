from datetime import datetime

from src.data import Data

import pandas as pd

startTime = datetime.now()
data = Data()
data.generate()
data.toDataFrame()


# display 'a' rows and 'b' columns of dataframe
a = len(data.df.index)
b = len(data.df.columns)
with pd.option_context('display.max_rows', a, 'display.max_columns', b):
    print(data.df)

print("\nExecution time: ", datetime.now() - startTime)
