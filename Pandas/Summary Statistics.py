# __author__ = Vishu Kamble
"""
A python program to learn summary statistics
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

arr = np.array(([1,2,np.nan],[np.nan,3,4]))
dframe = DataFrame(arr,index=['A','B'],columns=['One','Two','Three'])
print dframe

print dframe.sum()  # ignores null
print dframe.sum(axis=1)
print dframe.min()
print dframe.idxmin()
print dframe.max()
print dframe.idxmax()
print dframe.cumsum()
print dframe.describe()

