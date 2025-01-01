# Creating 2D Arrays using the numpy library

# import numpy as np
import numpy as np

# Create a 2D array of shape (3, 4) with random integers between 1 and 100
arr = np.random.randint(1, 100, (3, 4)) # Random integers between 1 and 100

# Print the 2D array
print(arr)


'''
CREATE A 2D array of shape (4, 4) and then insert it into the 2D array created
'''

arr = np.zeros((4,4), dtype=np.int32) # Create a 2D array of shape (4, 4) with zeros

# Insert the 2D array into the 2D array created
arr[0][0] = 1
arr[0][1] = 2
arr[0][2] = 3
arr[0][3] = 4
arr[1][0] = 5
arr[1][1] = 6
arr[1][2] = 7
arr[1][3] = 8
arr[2][0] = 9
arr[2][1] = 10
arr[2][2] = 11
arr[2][3] = 12
arr[3][0] = 13
arr[3][1] = 14
arr[3][2] = 15
arr[3][3] = 16

# Print the final 2D array
print(arr)

# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]


