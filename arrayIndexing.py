# __author__ = Vishu Kamble
"""
A python program to learn array indexing (Python 3)
"""

import numpy as np

arr = np.array([x for x in range(1, 11)])
print(arr)

print(arr[5])  # array index value
print(arr[1:4])  # slicing
print(arr[0:6])  # slicing
arr[0:4] = 4  # changing values
print(arr)

arr_copy = arr.copy()
arr_copy[:] = 0
print(arr_copy, arr)  # printing copy and original array

arr2 = np.array([[1, 2, 3], [7, 8, 9], [12, 14, 16]])  # creating new array
print(arr2)
print("Index 0: ", arr2[0])
print("\nInner values: ", arr2[0][1])

print(arr2[:2, 1:])


zero = np.zeros((10,10))
print(zero)

for i in range(len(zero)):
    zero[i] = i

print(zero)
