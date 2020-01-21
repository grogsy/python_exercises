# https://leetcode.com/problems/maximum-gap/submissions/

def maximumGap(nums: List[int]) -> int:
    max_gap = 0
    if len(nums) < 2:
        return max_gap

    nums.sort()
    i = 0
    j = len(nums) - 1

    while i < j:
        low_diff = nums[i + 1] - nums[i]
        high_diff = nums[j] - nums[j-1]

        local_max_diff = max(low_diff, high_diff)

        if local_max_diff > max_gap:
            max_gap = local_max_diff

        i += 1
        j -= 1

    return max_gap
