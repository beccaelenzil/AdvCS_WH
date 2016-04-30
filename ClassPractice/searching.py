def sequentialSearch(alist, val):
    for i in range(len(list)-1):
        if alist[i] == val:
            return True
    return False


# Number of Operations
# --------------------
# Best Case: 1 O(1)
# Worst Case: n O(n)
# Average Case: n/2 O(n)


def binarySearch(alist, val):
    check = len(alist)/2
    if alist[check] == val:
        return True
    elif len(alist) > 1:
        if val > alist[check]:
            return binarySearch(alist[check:], val)
        else:
            return binarySearch(alist[:check], val)
    else:
        return False


# Big-O of Binary Search
# Best: 1 O(1)
# Average: log(n)-1 O(log(n))
# Worst: log(n) O(log(n))