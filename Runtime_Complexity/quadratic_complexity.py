# Quadratic Runtime Complexity: O(n^2)

# Quadratic runtime complexity is the worst case scenario for an algorithm. It means that the runtime of an algorithm grows quadratically with the size of the input data set.

def sum_of_squares_quadratic(n):
    """
    This function calculates the sum of squares of the first n numbers 
    with quadratic time complexity.
    """
    sum = 0
    for i in range(1, n + 1):  # Outer loop
        for j in range(1, i + 1):  # Inner loop
            sum += i  # Simulate quadratic behavior
    return sum

if __name__ == '__main__':
    result = sum_of_squares_quadratic(10)
    print(result)


# Output: 385
