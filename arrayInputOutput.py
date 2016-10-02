# __author__ = Vishu Kamble
"""
A python program to see input output
"""
import numpy as np

arr = np.arange(5)
np.save('arrayInputOutput', arr)

arr = np.arange(10)
print("New array:", arr)

arr1 = np.load('arrayInputOutput.npy')
print("Loaded array: ", arr1)

arr2 = np.arange(10, 20)
arr3 = np.arange(30, 40)

np.savez('ziparray.npz', x=arr1, y=arr2, z=arr3)
archive_arrya = np.load('ziparray.npz')
print(archive_arrya['x'])
print(archive_arrya['y'])
print(archive_arrya['z'])

np.savetxt('myarray.txt',arr,delimiter=',')
arr = np.loadtxt('myarray.txt',delimiter=',')
print(arr)