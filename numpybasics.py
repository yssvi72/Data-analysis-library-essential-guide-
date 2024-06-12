#Numpy package to be installed
import numpy as np

# Creating a NumPy array 'x' containing elements 1, 2, 3, and 4
x = np.array([1, 2, 3, 4 , 5, 6])
print("Original array:")
print(x)

# Checking if none of the elements in the array 'x' is zero and printing the result
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

# Reassigning array 'x' to a new array containing elements 0, 1, 2, and 3
x = np.array([0, 1, 2, 3,4,5,6])

print(" Resizable  array:")
print(x)







