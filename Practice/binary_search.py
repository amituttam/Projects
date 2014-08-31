
def search(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return search(alist[mid+1:], item)
            else:
                return search(alist[:mid-1], item)

a = [0,1,2,3,4,5]
print(search(a,22))
