# Binary Search
# O(logn)


def binary_search(mylist, item):
    midpoint = len(mylist) // 2
    if len(mylist) == 0:
        return False
    if mylist[midpoint] == item:
        return True
    else:
        if item < mylist[midpoint]:
            return binary_search(mylist[:midpoint], item)
        else:
            return binary_search(mylist[midpoint + 1:], item)


print binary_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 41)
print binary_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 42)
