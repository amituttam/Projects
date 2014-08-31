
def bubble_sort(alist):
    for _ in range(len(alist)-1,0,-1):
        for i in range(_):
            if alist[i] > alist[i+1]:
                alist[i+1],alist[i] = alist[i],alist[i+1]
    return alist

alist = [10,2,3,11,23,0,1,4]
print(bubble_sort(alist))
