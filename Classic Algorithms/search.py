#!/usr/bin/env/python

def seq_search(alist, x):
    for i in range(len(alist)):
        if alist[i] == x:
            return True

    return False

def binary_search(alist, x):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == x:
            return True
        else:
            if x < alist[mid]:
                return binary_search(alist[:mid-1], x)
            else:
                return binary_search(alist[mid+1:], x)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
