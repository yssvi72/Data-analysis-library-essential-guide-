#Numpy package to be installed
import numpy as np

# Creating a NumPy array 'x' containing elements 1, 2, 3, and 4
x = np.array([1, 2, 3, 4 , 5, 6])
print("Original array:")
print(x)

# Checking if none of the elements in the array 'x' is zero and printing the result
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

#Shape of an numpy array
a = np.array([[1,2,3],[4,5,6]])
print('Array :','\n',a)
print('Shape :','\n',a.shape)
print('Rows = ',a.shape[0])
print('Columns = ',a.shape[1])





