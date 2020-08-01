# Problem Description
# The program takes a list and key as input and finds the index of the key in the list using binary search.

# Problem Solution
# 1. Create a function binary_search that takes a list and the variables start, end and key as arguments. The function searches for the key in the range [start… end – 1].
# 2. The base case consists of testing whether start is less than end. If not, -1 is returned.
# 3. mid is calculated as the floor of the average of start and end.
# 4. If the element at index mid is less than key, binary_search is called again wit start=mid + 1 and if it is more than key, it is called with end=mid. Otherwise, mid is returned as the index of the found element.

# Program/Source Code


def binary_search(alist, start, end, key):
    """Search key in alist[start... end - 1]."""
    if not start < end:
        return -1
 
    mid = (start + end)//2
    if alist[mid] < key:
        return binary_search(alist, mid + 1, end, key)
    elif alist[mid] > key:
        return binary_search(alist, start, mid, key)
    else:
        return mid
 
 
alist = input('Enter the sorted list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
 
index = binary_search(alist, 0, len(alist), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))


# Program Explanation
# 1. The user is prompted to enter a list of numbers.
# 2. The user is then asked to enter a key to search for.
# 3. The list and key is passed to binary_search with start=0 and end=length of the list.
# 4. If the return value is -1, the key is not found and a message is displayed, otherwise the index of the found item is displayed.

# Runtime Test Cases
# Case 1:
# Enter the sorted list of numbers: 4 5 6 7 8 9 10
# The number to search for: 9
# 9 was found at index 5.
 
# Case 2:
# Enter the sorted list of numbers: 3 4 5 10
# The number to search for: 8
# 8 was not found.
 
# Case 3:
# Enter the sorted list of numbers: 7
# The number to search for: 7
# 7 was found at index 0.