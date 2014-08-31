
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lhalf = alist[:mid]
        rhalf = alist[mid:]

        merge_sort(lhalf)
        merge_sort(rhalf)

        i,j,k=0,0,0
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[j]:
                alist[k] = lhalf[i]
                i += 1
            else:
                alist[k] = rhalf[j]
                j += 1
            k += 1

        while i < len(lhalf):
            alist[k] = lhalf[i]
            i+=1
            k+=1

        while j < len(rhalf):
            alist[k] = rhalf[j]
            j+=1
            k+=1
    return alist

print(merge_sort([1,4,0,9,34,5]))
