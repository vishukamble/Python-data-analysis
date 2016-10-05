# __author__ = Vishu Kamble
"""
A python program to 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

series = Series(randn(6), index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
print series

print series.index
print series[1]
print series[2]
print series[:,'a']
print series.unstack()

data = DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],columns=[['NY','NY','LA','SF'],['cold','hot','cold','hot']])
print data

data.index.names=['INDEX_1','INDEX_2']
data.columns.names=['Cities','Temp']
print data

data.swaplevel('Cities','Temp',axis=1)
print data

print data.sortlevel(1)

print data.sum(level='Temp',axis=1)