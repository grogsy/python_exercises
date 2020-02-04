# https://leetcode.com/problems/maximum-subarray/submissions/

def max_sub_array(nums):
    if len(nums) == 1:
        return nums[0]

    output = [nums[0]]

    for i in range(1, len(nums)):
        output.append(max(output[i - 1] + nums[i], nums[i]))

    return max(output)
