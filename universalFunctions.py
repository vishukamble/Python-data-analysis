# __author__ = Vishu Kamble
"""
A python program to learn universal functions
"""

import numpy as np

arr = np.array([x for x in range(6)])
print("\nDefault ", arr)
print("\nSquare root", np.sqrt(arr))
print("\nExponential", np.exp(arr))

arr2 = np.array([x*x for x in range(2, 8)])
print("\nSquare array: ",arr2)
# Binary functions
print("\nAdd ", np.add(arr, arr2))
print("\nMax ", np.maximum(arr, arr2))
print("\nMin ", np.minimum(arr, arr2))
