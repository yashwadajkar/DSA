# Lodarithmic Runtime Complexity: O(n^2)

# Logarithmic Complexity for an algorithm is the second best case scenario for an algorithm. It means that the runtime of an algorithm grows logarithmically with the size of the input data set.

def binary_search(arr, target):
    """
    Perform binary search to find the target in the sorted array.
    Returns the index of the target if found, otherwise -1.
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Target not found

if __name__ == '__main__':
    sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    target = 10
    result = binary_search(sorted_array, target)
    print(f"Target {target} found at index: {result}")

# Output: Target 10 found at index: 4