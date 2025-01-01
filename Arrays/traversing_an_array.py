# Traversing the numpy array
# You can traverse a numpy array using a for loop. Here's an example:

# import numpy as np
import numpy as np

# Create a numpy array of length 5 with integers
arr = np.array([10, 20, 30, 40, 50])

# Print the array
print(arr)

# Traverse the array
for elements in arr:
    print(elements)

# Output:
# [10 20 30 40 50]


# Accessing the numpy array elements using index
# You can access the elements of a numpy array using the index. Here's an example:

print(arr[0])  # Output: 10


# Finding the elements of a numpy array
# You can find the elements of a numpy array using the where() function. Here's an example:

indices = np.where(arr == 30)
print(indices)  # Output: (array([2]),) 10