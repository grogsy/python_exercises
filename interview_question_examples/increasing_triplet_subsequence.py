# https://leetcode.com/problems/increasing-triplet-subsequence/

def increasingTriplet(nums):
    if len(nums) >= 3:
        low = 0
        length = len(nums) - 1
        high = len(nums) - 1

        current_min = nums[low]
        current_max = nums[high]

        while low < high:
            next_low = nums[low + 1]
            next_high = nums[high - 1]

            # check any digit i between min and max that satisfies min < i < max
            check_low = next_low > current_min and next_low < current_max
            check_high = next_high < current_max and next_high > current_min
            not_contiguous = current_min < current_max and (check_low or check_high)

            check_low_ahead = nums[low] < next_low and next_low < nums[low + 2]
            check_high_ahead = nums[high] > next_high and next_high > nums[high - 2]
            ahead_contiguous = check_low_ahead or check_high_ahead

            check_low_trailing = low - 1 >= 0 and (nums[low] > nums[low - 1] and nums[low - 1] < current_min)
            check_high_trailing = high + 1 < length and (nums[high] < nums[high + 1] and nums[high + 1] < current_max)
            trailing_contiguous = check_low_trailing or check_high_trailing

            if not_contiguous or ahead_contiguous or trailing_contiguous:
                return True
                
            if next_low < current_min:
                current_min = next_low
            if next_high > current_max:
                current_max = next_high

            low += 1
            high -= 1

    return False
