# Problem Description
# The program takes a list and key as input and finds the index of the key in the list using binary search.

# Problem Solution
# 1. Create a function binary_search that takes a list and key as arguments.
# 2. The variable start is set to 0 and end is set to the length of the list.
# 3. The variable start keeps track of the first element in the part of the list being searched while end keeps track of the element one after the end of the part being searched.
# 4. A while loop is created that iterates as long as start is less than end.
# 5. mid is calculated as the floor of the average of start and end.
# 6. If the element at index mid is less than key, start is set to mid + 1 and if it is more than key, end is set to mid. Otherwise, mid is returned as the index of the found element.
# 7. If no such item is found, -1 is returned.

# Program/Source Code


def binary_search(alist, key):
    """Search key in alist[start... end - 1]."""
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end)//2
        if alist[mid] > key:
            end = mid
        elif alist[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1
 
 
alist = input('Enter the sorted list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
 
index = binary_search(alist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))


# Program Explanation
# 1. The user is prompted to enter a list of numbers.
# 2. The user is then asked to enter a key to search for.
# 3. The list and key is passed to binary_search.
# 4. If the return value is -1, the key is not found and a message is displayed, otherwise the index of the found item is displayed.

# Runtime Test Cases
# Case 1:
# Enter the sorted list of numbers: 3 5 10 12 15 20
# The number to search for: 12
# 12 was found at index 3.
 
# Case 2:
# Enter the sorted list of numbers: -3 0 1 5 6 7 8
# The number to search for: 2
# 2 was not found.
 
# Case 3:
# Enter the sorted list of numbers: 5
# The number to search for: 5
# 5 was found at index 0.