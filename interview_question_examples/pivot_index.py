# https://leetcode.com/problems/find-pivot-index

def pivotIndex(nums):
    if not nums: return -1

    pivot_index = 0
    sum_left = 0
    sum_right = sum(nums) - nums[pivot_index]


    while pivot_index < len(nums) - 1:
        if sum_left == sum_right:
            return pivot_index

        sum_left += nums[pivot_index]
        pivot_index += 1
        sum_right -= nums[pivot_index]

    return pivot_index if sum_left == sum_right else -1pivot_



    # slow version
#         while pivot_index < len(nums):
#             sum_left = sum(nums[:pivot_index])
#             sum_right = sum(nums[pivot_index + 1:])

#             if sum_left == sum_right:
#                 return pivot_index

#             pivot_index += 1

#         return -1
