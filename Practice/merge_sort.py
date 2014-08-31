
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lhalf = alist[:mid]
        rhalf = alist[mid:]

        merge_sort(lhalf)
        merge_sort(rhalf)

        # Perform sort
        i,j,k = 0,0,0
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[j]:
                alist[k] = lhalf[i]
                i += 1
            else:
                alist[k] = rhalf[j]
                j += 1
            k += 1

        # Handle rest
        while i < len(lhalf):
            alist[k] = lhalf[i]
            i += 1
            k += 1

        while j < len(rhalf):
            alist[k] = rhalf[j]
            j += 1
            k += 1

    return alist

a = [12,23,0,11,4,3,4,2,1]
print merge_sort(a)
