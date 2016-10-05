# __author__ = Vishu Kamble
"""
A python program to learn drop entry
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series = Series(np.arange(5),index=['a','b','c','d','e'])
print series

print series.drop('c')

frame = DataFrame(np.arange(9).reshape((3,3)),index=['Hob', 'Chi', 'NY'], columns=['Pop','Size','Year'])
print frame

print frame.drop('NY')
print frame.drop('Year',axis=1)