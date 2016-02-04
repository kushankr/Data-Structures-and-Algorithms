# Merge Sort and Quick Sort Algoritms
# Both O(nlogn) - QuickSort has better space complexity


def Merge(L, R, A):
    nL = len(L)
    nR = len(R)

    i = 0
    j = 0
    k = 0

    while i < nL and j < nR:
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
            k = k + 1

        elif R[j] < L[i]:
            A[k] = R[j]
            j = j + 1
            k = k + 1

    while i < nL:
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j < nR:
        A[k] = R[j]
        j = j + 1
        k = k + 1

    return A


def Mergesort(mylist):
    midpoint = len(mylist) // 2
    if len(mylist) < 2:
        return
    else:
        L = mylist[:midpoint]
        R = mylist[midpoint:]
        Mergesort(L)
        Mergesort(R)
        Merge(L, R, mylist)

        return mylist


print Mergesort([7, 2, 1, 6, 8, 5, 3, 4])


def partition(mylist, start, end):
    pivot = mylist[end]
    pindex = 0
    i = 0

    while i < end:

        if mylist[i] > pivot:
            pindex = pindex
            i = i + 1

        elif mylist[i] < pivot:
            temp = mylist[pindex]
            mylist[pindex] = mylist[i]
            mylist[i] = temp

            pindex = pindex + 1
            i = i + 1

    temp = mylist[pindex]
    mylist[pindex] = mylist[i]
    mylist[i] = temp

    return pindex


def quicksort(myarr, start, end):
    if start < end:
        pindex = partition(myarr, start, end)
        quicksort(myarr, start, pindex - 1)
        quicksort(myarr, pindex + 1, end)

    return myarr


A = [7, 2, 1, 6, 8, 5, 3, 4]
print quicksort(A, 0, len(A) - 1)
