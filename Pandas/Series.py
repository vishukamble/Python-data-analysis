# __author__ = Vishu Kamble
"""
A python program to learn Series
"""
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

obj = Series([2, 4, 6, 8])
print obj
print obj.index

war_cas = Series([8700000, 4300000, 300000, 210000, 400000], index=['USSR', 'Germany', 'China', 'Japan', 'USA'])
print war_cas
print war_cas['China']
print war_cas[war_cas > 400000]
print 'USA' in war_cas

# Convert to dic
ww_caseDict = war_cas.to_dict()
print ww_caseDict

# Convert dict to series
ww_caseSeries = Series(ww_caseDict)
print ww_caseSeries


l = ['USSR', 'Germany', 'China', 'Japan', 'USA', 'Argentina']
obj2 = Series(ww_caseDict, index=l)
obj2.name = "World War 2 Casualties"
obj2.index.name = 'Countries'
print obj2

print ww_caseSeries+obj2