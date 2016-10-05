# __author__ = Vishu Kamble
"""
A python program to learn data Alignemnet
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series = Series([0, 1, 2], index=['A', 'B', 'C'])
print series

series2 = Series([3, 4, 5, 6], index=['A', 'B', 'C', 'D'])
print series + series2

dframe = DataFrame(np.arange(4).reshape((2,2)),columns=list('AB'), index=['NYC', 'CHI'])
print dframe

dframe2 = DataFrame(np.arange(9).reshape((3,3)),columns=list('ADC'), index=['NYC', 'CHI', 'LA'])
print dframe2

print dframe.add(dframe2, fill_value=0)

invert = dframe2.ix[0]
print dframe2

print dframe2 - invert
