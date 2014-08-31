#!/usr/bin/env python

def bubble_sort(nums):
    # Number of passes
    for _ in range(len(nums)-1,0,-1):
        for j in range(_):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        print nums

    return nums

def merge_sort(nums):
    print "Splitting",nums

    if len(nums) > 1:
        # Get midpoint, lefthalf, and righthalf lists
        mid = len(nums)//2
        lhalf = nums[:mid]
        rhalf = nums[mid:]

        # Merge sort left and right halves
        merge_sort(lhalf)
        merge_sort(rhalf)

        # Sort the right and left halves
        i,j,k = 0,0,0
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[j]:
                nums[k] = lhalf[i]
                i += 1
            else:
                nums[k] = rhalf[j]
                j += 1
            k += 1

        # Handle remaining halves
        while i < len(lhalf):
            nums[k] = lhalf[i]
            i += 1
            k += 1

        while j < len(rhalf):
            nums[k] = rhalf[j]
            j += 1
            k += 1

    print "Merging",nums
    return nums

def quick_sort(nums):
    _quick_sort(nums, 0, len(nums)-1)

def _quick_sort(nums, first, last):
    if first < last:
        splitpoint = partition(nums, first, last)

        _quick_sort(nums, first, splitpoint-1)
        _quick_sort(nums, splitpoint+1, last)

def partition(nums, first, last):
    pivotval = nums[first]
    lmark = first+1
    rmark = last

    done = False
    while not done:
        while lmark <= rmark and nums[lmark] <= pivotval:
            lmark += 1

        while rmark >= lmark and nums[rmark] >= pivotval:
            rmark -= 1

        if rmark < lmark:
            done = True
        else:
            nums[lmark],nums[rmark] = nums[rmark],nums[lmark]

    nums[first],nums[rmark] = nums[rmark],nums[first]
    return rmark
    
nums = [9,3,1,10,23,1,0]
print(nums)
#print "Bubble Sort:"
#print(bubble_sort(nums))
#print "Merge Sort:"
#print(merge_sort(nums))
quick_sort(nums)
print(nums)
