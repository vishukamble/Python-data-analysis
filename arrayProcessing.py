# __author__ = Vishu Kamble
"""
A python program to plot arrays
"""
import inline as inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

points = np.array([-5, 5, 0.01])
dx, dy = np.meshgrid(points, points)
print(dx, dy)
z = np.sin(dx) + np.sin(dy)
print("\n\n", z)

plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin x and sin y')

arr = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])
condition = np.array([True, True, False, False])
answer = [(arr_val if condition else arr2_val) for arr_val, arr2_val, condition in zip(arr, arr2, condition)]
print(answer)

answer2 = np.where(condition, arr, arr2)
print(answer2)

from numpy.random import randn

arr = randn(5, 5)
print(arr)

print("\n\n", np.where(arr < 0, 0, arr))  # Turn all negs to 0

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\npriting sums: \n")
print(arr.sum())
print(arr[0].sum())
print(arr[1].sum())
print(arr.mean())
print(arr.std())
print(arr.var())

print("\nSorting")
arr = randn(5)
print(arr)
arr = arr.sort()
print(arr)

print("\nUnique")
arr = ['A', 'B', 'B', 'C', 'E', 'A', 'F', 'G']
print(np.unique(arr))
print (np.in1d(['A','X','B','E'],arr))

"""
[[-5.    5.    0.01]
 [-5.    5.    0.01]
 [-5.    5.    0.01]] [[-5.   -5.   -5.  ]
 [ 5.    5.    5.  ]
 [ 0.01  0.01  0.01]]


 [[ 1.91784855  0.          0.96892411]
 [ 0.         -1.91784855 -0.94892444]
 [ 0.96892411 -0.94892444  0.01999967]]
[1, 2, 30, 40]
[ 1  2 30 40]
[[-1.04367862  1.49436458 -0.02797558  1.4099805  -0.21923396]
 [ 0.62113927  0.74512155  1.71598141  1.8976417   2.78668151]
 [-0.20567368  1.09051748  0.44884563 -1.29234248  1.99783157]
 [ 0.85082928 -0.43475611  1.13221727 -0.68256639  0.94931255]
 [-0.08267199 -0.47675859  1.67101208 -0.36895092  0.27094526]]


 [[ 0.          1.49436458  0.          1.4099805   0.        ]
 [ 0.62113927  0.74512155  1.71598141  1.8976417   2.78668151]
 [ 0.          1.09051748  0.44884563  0.          1.99783157]
 [ 0.85082928  0.          1.13221727  0.          0.94931255]
 [ 0.          0.          1.67101208  0.          0.27094526]]

priting sums:

45
6
15
5.0
2.58198889747
6.66666666667

Sorting
[ 0.53218323 -0.03503038  0.62534766  0.49454049  1.50079124]
None

Unique
['A' 'B' 'C' 'E' 'F' 'G']
[ True False  True  True]
"""