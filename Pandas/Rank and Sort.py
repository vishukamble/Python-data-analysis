# __author__ = Vishu Kamble
"""
A python program to learn Rank and Sort
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series = Series(range(4), index=['C','A','E','D'])
print series.sort_index
print series.order()

series2 = Series([12,9,3,14,2,54])
print series2.sort()
print series2.rank()

