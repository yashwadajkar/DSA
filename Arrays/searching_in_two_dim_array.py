# Searching in 2D arrays using the numpy library

# import numpy as np
import numpy as np

# Create a 2D array of shape (3, 4) with random integers between 1 and 100
arr = np.random.randint(1, 100, (3, 4))  # Random integers between 1 and 100
print(arr)

# Search for a specific element in the 2D array
element = 50
found = False

# Iterate over each row in the 2D array
for i in range(3):
    # Iterate over each element in the row
    for j in range(4):
        # Check if the element is found
        if arr[i][j] == element:
            found = True
            break
        elif arr[i][j] != element:
            continue

print(found)