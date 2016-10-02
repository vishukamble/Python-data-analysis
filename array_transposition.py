# __author__ = Vishu Kamble
"""
A python program to learn transposition
"""
import numpy as np

arr = np.array([x for x in range(50)]).reshape(10,5)
print(arr)
x = arr.T  #transpose
print(np.dot(x,arr))