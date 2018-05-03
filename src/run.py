import pandas as pd
import numpy as np


from src.data import Data

data = Data()
data.generate()

#Adding empty row for 'Value'
newData = np.append(data.x, np.zeros((1, data.m)), axis=0)
df = pd.DataFrame(data=newData, index=['X', 'Y', 'Value'])

#Display 'a' rows and 'b' columns of data
a = len(df.index)
b = len(df.columns)
with pd.option_context('display.max_rows', a, 'display.max_columns', b):
    print(df)