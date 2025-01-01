# Deletion in 2D array with numpy arrays

# import numpy as np
import numpy as np

# Create a 2D array of shape (3, 4) with random integers between 1 and 100
arr = np.random.randint(1, 100, (3, 4))  # Random integers between 1 and 100
print(arr)

# Delete the first row from the 2D array
arr = np.delete(arr, 0, axis=0) # Delete the first row 


print("\nResult after deletion : \n")

# Print the modified 2D array
print(arr)