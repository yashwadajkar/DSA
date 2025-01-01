# Basic numpy functions for creating arrays and array operations for numerical computations.

# import numpy
import numpy as np

# Create an array of length 5 with integers
arr = np.array([10, 20, 30, 40, 50])

# Print the array
print(arr)

# Output: [10 20 30 40 50]

# Create an array of length 5 with zeros
arr = np.zeros(5)
print(arr)

# Output: [0. 0. 0. 0. 0.]

# Create an array of length 5 with ones
arr = np.ones(5)
print(arr)

# Output: [1. 1. 1. 1. 1.]

# Create an array of length 5 with random values
arr = np.random.rand(5)
print(arr)

# Output: [0.50528907 0.48635299 0.83371767 0.05619652 0.26875666]

# Create an array of length 5 with a specific value
arr = np.full(5, 10)
print(arr)

# Output: [10 10 10 10 10]

# Create an array of length 5 with a range of values
arr = np.arange(5)
print(arr)

# Output: [0 1 2 3 4]

# Create an array of length 5 with a range of values with a step size
arr = np.arange(0, 10, 2)
print(arr)

# Output: [0 2 4 6 8]

# Print the size of the array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr1.size)

# Output: 8


# Array operations
# Perform element-wise addition
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
arr_sum = arr1 + arr2
print(arr_sum)

# Output: [ 7  9 11 13 15]  

# Perform element-wise subtraction
arr_diff = arr1 - arr2
print(arr_diff)

# Output: [-5 -5 -5 -5 -5]


# Perform element-wise multiplication
arr_mul = arr1 * arr2
print(arr_mul)

# Output: [ 6 14 24 36 50]

# Perform element-wise division

arr_div = arr2 / arr1
print(arr_div)

# Output: [ 6.  6.  6.  6.  6.]

# Perform element-wise power operation
arr_power = arr1 ** 2
print(arr_power)

# Output: [ 1  4  9 16 25]

# Perform element-wise square root operation
arr_sqrt = np.sqrt(arr1)
print(arr_sqrt)

# Output: [1.         1.41421356 1.73205081 2.         2.23606798]