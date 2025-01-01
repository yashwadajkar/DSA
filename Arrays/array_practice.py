# Practice the following operations on arrays in python using numpy arrays:

# import numpy as np
import numpy as np

# 1. Create an array and traverse. 

arr1 = np.array([10,20,30,40,50])

for i in range (0, np.size(arr1)):
    print(arr1[i])

# 2. Access individual elements through indexes

arr2 = np.array([10,20,30,40,50])

print(arr2[0])
print(arr2[1])
print(arr2[2])
print(arr2[3])
print(arr2[4])

# 3. Append any value to the array

arr3 = np.array([10,20,30,40,50])
arr3 = np.append(arr3, 60)
print(arr3)

# 4. Insert value in an array using insert() method

arr4 = np.array([10,20,30,40,50])
arr4 = np.insert(arr4, 2, 25)
print(arr4)

# 5. Extend python array using extend() method

arr5 = np.array([10,20,30,40,50])
arr5 = np.append(arr5, [60, 70, 80])
print(arr5)

# 6. Add items from list into array

list = [60, 70, 80]
arr6 = np.array([10,20,30,40,50])
arr6 = np.append(arr6, list)
print(arr6)

# 7. Remove any array element

arr7 = np.array([10,20,30,40,50])
arr7 = np.delete(arr7, 4)
print(arr7)

# 8. Remove last array element

arr8 = np.array([10,20,30,40,50])
arr8 = np.delete(arr8, -1)
print(arr8)

# 9. Fetch any element through its index

arr9 = np.array([10,20,30,40,50])
print(arr9[2])

# 10. Reverse a python array

arr10 = np.array([10,20,30,40,50])
print(arr10[::-1])

# 11. Get array buffer information

arr11 = np.arange(10)
print(arr11)
print(arr11.data)

# 12. Check for number of occurrences of an element using count() method

arr12 = np.array([10,20,30,40,50,10,20,30,40,50])
print(np.count_nonzero(arr12 == 10))

# 13. Convert array to string

arr13 = np.array([10,20,30,40,50])
print(arr13.tostring())


# 14. Convert array to a python list with same elements

arr14 = np.array([10,20,30,40,50])
print(arr14.tolist())

# 15. Append a string to char array

arr15 = np.array(['a', 'b', 'c', 'd', 'e'])
arr15 = np.append(arr15, 'f')
print(arr15)

# 16. Slice Elements from an array

arr16 = np.array([10,20,30,40,50])
print(arr16[1:4])