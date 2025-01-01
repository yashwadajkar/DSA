# Traversing 2D arrays with numpy arrays

# import numpy as np
import numpy as np

# Create a 2D array of shape (3, 4) with random integers between 1 and 100
arr = np.random.randint(1,100, (3,4)) # Random integers between 1 and 100
print(arr)

for i in range(3):
    for j in range(4):
        print(f"arr[{i}][{j}] = ", arr[i][j])
    print("\n")