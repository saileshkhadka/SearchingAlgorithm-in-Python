# Problem Description
# The program takes a list and i as input and prints the ith smallest element in the list.

# Problem Solution
# 1. Create a function select which takes a list and variables start, end, i as arguments.
# 2. The function will return the ith smallest element in the range alist[start… end – 1].
# 3. The base case consists of checking whether there is only one element in the list and if so, alist[start] is returned.
# 4. Otherwise, the list is partitioned using Hoare’s partitioning scheme.
# 5. If i is equal to the number of elements in alist[start… pivot], call it k, then the pivot is the ith smallest element.
# 6. Otherwise, depending on whether i is greater or smaller than k, select is called on the appropriate half of the list.

# Program/Source Code


def select(alist, start, end, i):
    """Find ith smallest element in alist[start... end-1]."""
    if end - start <= 1:
        return alist[start]
    pivot = partition(alist, start, end)
 
    # number of elements in alist[start... pivot]
    k = pivot - start + 1
 
    if i < k:
        return select(alist, start, pivot, i)
    elif i > k:
        return select(alist, pivot + 1, end, i - k)
 
    return alist[pivot]
 
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
 
 
alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
i = int(input('The ith smallest element will be found. Enter i: '))
 
ith_smallest_item = select(alist, 0, len(alist), i)
print('Result: {}.'.format(ith_smallest_item))


# Program Explanation
# 1. The user is prompted to enter a list of numbers.
# 2. The user is then asked to enter i.
# 3. The ith smallest element is found by calling select.
# 4. The result is displayed.

# Runtime Test Cases
# Case 1:
# Enter the list of numbers: 3 5 10 2 -1 0 2
# The ith smallest element will be found. Enter i: 2
# Result: 0.
 
# Case 2:
# Enter the list of numbers: 7
# The ith smallest element will be found. Enter i: 1
# Result: 7.
 
# Case 3:
# Enter the list of numbers: 5 4 3 2 1
# The ith smallest element will be found. Enter i: 5
# Result: 5.