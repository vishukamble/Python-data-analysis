# __author__ = Vishu Kamble
"""
A python program to find missing data
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = Series(['one','two',np.nan,'four'])
print data.isnull()
print data.dropna()

dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,8],[np.nan, np.nan, np.nan]])
print dframe

cleandFrame = dframe.dropna()
print cleandFrame

print dframe.dropna(how='all')
print dframe.dropna(axis=1)

npn = np.nan
dframe2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,8],[1,npn,npn,npn]])
print dframe2

print dframe2.dropna(thresh=2)
print dframe2.dropna(thresh=3)
print dframe2.fillna(1)
print dframe2.fillna({0:0,1:1,2:2,3:3})

dframe2.fillna(0,inplace=True)
print dframe2