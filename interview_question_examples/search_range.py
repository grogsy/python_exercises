# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(nums, target):
    target_index = bins(nums, target, 0, len(nums) - 1)
    
    if target_index == -1:
        return [-1, -1]

    return scan(nums, target_index, target)
    
def bins(nums, target, low, high):
    if low > high:
        return -1

    pivot = high + low // 2
    if nums[pivot] == target:
        return pivot
    elif nums[pivot] < target:
        low = pivot + 1
    elif nums[pivot] > target:
        high = pivot - 1

    return bins(nums, target, low, high)
    
def scan(nums, index, target):
    # scan left and right for the first and last pos of target

    left = right = index
    while left > 0 and nums[left - 1] == target:
        left -= 1

    while right < len(nums) - 1 and nums[right + 1] == target:
        right += 1

    return [left, right]
