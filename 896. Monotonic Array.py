from time import time
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev = nums[0]
        sign = 0
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue
            if nums[i] < prev:
                if sign == 1:
                    return False
                sign = -1
            else:
                if sign == -1:
                    return False
                sign = 1
            prev = nums[i]
        return True


start_time = time()

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true
#
# Example 2:
# Input: nums = [6,5,4,4]
# Output: true
#
# Example 3:
# Input: nums = [1,3,2]
_nums = [1,3,2]
# Output: false

print(Solution().isMonotonic(_nums))

print("--- %s seconds ---" % (time() - start_time))
