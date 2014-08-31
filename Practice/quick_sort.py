
def quick_sort(alist):
    _quick_sort(alist, 0, len(alist)-1)

def _quick_sort(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        _quick_sort(alist, first, splitpoint-1)
        _quick_sort(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivot = alist[first]
    lmark = first + 1
    rmark = last

    done = False
    while not done:
        while lmark <= rmark and nums[lmark] <= pivot:
            lmark += 1

        while rmark >= lmark and nums[rmark] >= pivot:
            rmark -= 1

        if rmark < lmark:
            done = True
        else:
            nums[lmark],nums[rmark] = nums[rmark],nums[lmark]

    nums[first],nums[rmark] = nums[rmark],nums[first]
    return rmark

nums = [1,0,2,3,4,5]
quick_sort(nums)
print nums
