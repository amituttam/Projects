
def bubble_sort(alist):
    for _ in range(len(alist)-1,0,-1):
        for i in range(_):
            if alist[i] > alist[i+1]:
                alist[i+1],alist[i] = alist[i],alist[i+1]
    return alist

print(bubble_sort([1,4,2,3,9,0]))
