# __author__ = Vishu Kamble
"""
A python program to 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series = Series(np.arange(3),index=['A','B','C'])
series = 2 * series
print series

print series[1]
print series['B']
print series[0:3]
print series['A':'B']
series[series>3] = 10
print series

dframe = DataFrame(np.arange(25).reshape((5,5)),index=["NYC", "LA", "SF", "CHI", "DC"],
                   columns=['A','B','C','D','E'])

print dframe
print dframe[dframe['D']>8]
print dframe>10