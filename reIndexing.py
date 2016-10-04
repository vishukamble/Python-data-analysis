# __author__ = Vishu Kamble
"""
A python program to learn reindexing
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from numpy.random import randn

series = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
print "Series: ", series

series2 = series.reindex(['A', 'B', 'C', 'D', 'E', 'F'])
print "Series 2: ", series2

print "Fill value: ", series2.reindex(['A', 'B', 'C', 'D', 'E', 'F', 'G'], fill_value=0)
series3 = Series(['India', 'USA', 'Canada'], index=[0, 5, 10])
print series3

print series3.reindex(range(15), method='ffill')

dframe = DataFrame(randn(25).reshape((5, 5)), index=['A', 'B', 'D', 'E', 'F'],
                   columns=['col1', 'col2', 'col3', 'col4', 'col5'])

cols = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6']
print dframe.ix[['A','B','C','D','E','F'],cols]