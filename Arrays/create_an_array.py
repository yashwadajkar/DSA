# Create a new array of length 5 and print all elements

# import array
import array

# Create an array of length 5 with integers
arr = array.array('i', [10, 20, 30, 40, 50])

# Note: here "i" is the typecode for integer which is used to create an array of integers.

# Print all elements of the array
for elements in arr:
    print(elements)

# For numerical computations, libraries like NumPy are preferred, which are more powerful and versatile than the array module.
# For general-purpose programming, Python's list is usually sufficient.