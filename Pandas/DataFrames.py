# __author__ = Vishu Kamble
"""
A python program to learn DataFrames
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser

# website = "https://en.wikipedia.org/wiki/List_of_Arsenal_F.C._records_and_statistics"
# webbrowser.open(website)

arsenal_frame = pd.read_clipboard()
print arsenal_frame
print arsenal_frame.Name
print arsenal_frame["FA Cup"]

multiple_cols = DataFrame(arsenal_frame, columns=['#', 'Name', 'Years', 'Leaguea'])
print multiple_cols

print arsenal_frame.head(3)  # Give first 3 rows
print arsenal_frame.tail(5)  # Give last 5 rows

print arsenal_frame.ix[4]
arsenal_frame['Manager'] = 'Arsene Wenger'

print arsenal_frame

data = {'City': ['Chicago', 'NYC', 'LA'], 'Population': ['83700', '1000000', '1233445']}
city_frame = DataFrame(data)
print city_frame


