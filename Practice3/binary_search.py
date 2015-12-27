#!/usr/bin/python

def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return binary_search(alist[mid+1:], item)
            else:
                return binary_search(alist[:mid], item)
