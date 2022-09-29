from time import time
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first_max, second_max = -1, -1
        i_max = 0
        for i, num in enumerate(nums):
            if num > first_max:
                first_max, second_max = num, first_max
                i_max = i
            elif num > second_max:
                second_max = num
        return i_max if second_max * 2 <= first_max else -1


start_time = time()

_nums = [3,6,1,0]
# Example 1:
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.

print(Solution().dominantIndex(_nums))

print("--- %s seconds ---" % (time() - start_time))
