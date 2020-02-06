# https://leetcode.com/problems/longest-consecutive-sequence/submissions/

def longestConsecutive(nums):
    if not nums:
        return 0

    longest_count = count = 1
    prev_num = nums.pop(nums.index(min(nums)))

    while nums:
        current_num = nums.pop(nums.index(min(nums)))
        if current_num - prev_num != 1:
            if prev_num == current_num:
                continue
            else:
                if count > longest_count:
                    longest_count = count
                count = 0

        prev_num = current_num
        count += 1

    if count > longest_count:
        return count

    return longest_count
