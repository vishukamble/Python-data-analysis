# __author__ = Vishu Kamble
"""
A python program to learn indexing objects
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series = Series([1,2,3,4], index=['A','B','C','D'])
print series

my_index = series.index
print my_index

print my_index[1]
print my_index[2:]