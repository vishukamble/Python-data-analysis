# __author__ = Vishu Kamble
"""
A python program to learn arrays using numpy (Python 3)
"""

import numpy as np

l1 = [1, 2, 3, 4]
arr1 = np.array(l1)
print(arr1)

l2 = [15, 30, 45, 60]

lCombined = [l1, l2]

arr2 = np.array(lCombined)
print()
print(arr2)

print("Shape is: ", arr2.shape)   #Show shape
print("Type is: ", arr2.dtype)   #Show data type
print()
print("matrix: ", np.ones([5, 5]))  # Matrix of 5x5 consisting of 1s
print()
print(np.empty(5))
