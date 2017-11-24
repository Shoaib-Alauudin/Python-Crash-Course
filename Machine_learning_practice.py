# import numpy as np
#
# # print((np.arange(1,101).reshape(10,10))/100)
#
# mat = np.arange(1,26).reshape(5,5)
# print(mat)
#
# print("--------------")
# print(mat.sum())
# print(mat.std())
# print(mat.sum(axis = 1))

import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5,4),[1,2,3,4,5],['A','B','C','D'])
bool_df = df < 0
print(df[df['B'] < 0][['A','D']])




