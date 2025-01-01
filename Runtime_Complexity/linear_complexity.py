# Linear Runtime Complexity: O(n)

# Linear runtime complexity is the most common case for an algorithm. It means that the runtime of an algorithm grows linearly with the size of the input data set.

def sum_of_n_numbers(n):
    
    """
    This function returns the sum of the first n numbers.
    """
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

if __name__ == '__main__':
    print(sum_of_n_numbers(10))

# Output: 55