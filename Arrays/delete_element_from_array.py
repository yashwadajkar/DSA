# Delete an element from an array (numpy array)

# import numpy
import numpy as np

# Create an array of length 5 with integers
arr = np.array([10, 20, 30, 40, 50])

# Print the original array
print(arr)

# Output the original array
# [10 20 30 40 50]



"""
DELETE AN ELEMENT FROM THE BEGINNING OF THE ARRAY (numpy array)
"""

# Delete the first element of the array
arr = np.delete(arr, 0)

# Print the updated array
print(arr)

# Output the updated array
# [20 30 40 50]



"""
DELETE AN ELEMENT FROM THE END OF THE ARRAY (numpy array)
"""

# Delete the last element of the array
arr = np.delete(arr, -1)

# Print the updated array
print(arr)

# Output the updated array
# [20 30 40]



"""
DELETE AN ELEMENT AT A GIVEN INDEX (numpy array)
"""

# Delete the element at index 1
arr = np.delete(arr, 1)

# Print the updated array
print(arr)

# Output the updated array
# [20 40 50]


"""
DELETE ALL ELEMENTS (numpy array)
"""

# Delete all elements from the array
arr = np.delete(arr, np.s_[:])

# Print the updated array
print(arr)

# Output the updated array
# []