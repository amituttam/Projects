def quick_sort(alist):
    _quick_sort(alist, 0, len(alist))

def _quick_sort(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        _quick_sort(alist, first, splitpoint-1)
        _quick_sort(alist, splitpoint+1, last)
