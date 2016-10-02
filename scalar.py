# __author__ = Vishu Kamble
"""
A python program to se scalars and arrays (Python 3)
"""

import numpy as np

arr1 = np.array([[1, 2, 3, 4], [10, 20, 30, 40]])
print(arr1)
print("\n", np.shape(arr1))  # (2,4)

print("\n", arr1 * arr1)
print("\n", arr1 - arr1)
print("\n", 1 / arr1)
print("\n", arr1**4)
