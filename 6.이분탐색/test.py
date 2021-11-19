def min_upper_bound(nums,i):
    start ,end = 0, len(nums)
    index = 0
    while start<=end:
        mid = (start+end)//2
        if nums[mid]<i:
            start = mid+1
            index = mid
        else:
            end = mid-1
    return index

def min_lower_bound(nums,i):
    start ,end = 0, len(nums)
    index = 0
    while start<=end:
        mid = (start+end)//2
        if nums[mid]<=i:
            start = mid+1
            index = mid
        else:
            end = mid-1
    return index

def lower_bound(nums,i):
    start ,end = 0, len(nums)
    index = 0
    while start<=end:
        mid = (start+end)//2
        if nums[mid]>=i:
            end = mid-1
            index = mid
        else:
            start = mid+1
    return index

def upper_bound(nums,i):
    start ,end = 0, len(nums)
    index = 0
    while start<=end:
        mid = (start+end)//2
        if nums[mid]>i:
            end = mid-1
            index = mid
        else:
            start = mid+1
    return index

nums = [3,4,4,6]
print(min_upper_bound(nums,4)) #0 target보다 작은값이     나오는 마지막 index
print(min_lower_bound(nums,4)) #2 target보다 작거나같은값이 나오는 마지막 index

print(lower_bound(nums,4)) #1 target보다 크거나같은값이 처음나오는 index
print(upper_bound(nums,4)) #3 target보다 큰값이       처음나오는 index