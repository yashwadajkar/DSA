# Insert an element in an array (numpy array)

# import numpy
import numpy as np

# Create an array of length 5 with integers
arr = np.array([10, 20, 30, 40, 50])

# Print the original array
print(arr)

# Output the original array
# [10 20 30 40 50]



"""
INSERT AN ELEMENT IN THE BEGINNING OF THE ARRAY (numpy array)
"""

new_element = 0
arr = np.insert(arr, 0, 0)

# Print the updated array
print(arr)

# Output the updated array
# [ 0 10 20 30 40 50]




"""
INSERT AN ELEMENT IN THE END OF THE ARRAY (numpy array)
"""

# Insert a new element in the end of the array
new_element = 60
arr = np.append(arr, new_element)

# Print the updated array
print(arr)


# Output the updated array
# [ 0 10 20 30 40 50 60]



"""
INSERT AN ELEMENT AT A GIVEN INDEX (numpy array)
"""

# Insert a new element at index 3
new_element = 35
arr = np.insert(arr, 3, new_element)

# Print the updated array
print(arr)

# Output the updated array
# [ 0 10 20 35 30 40 50 60]