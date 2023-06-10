from time import time
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        cur_min, cur_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur_min, cur_max = min(num, cur_min, cur_min * num, cur_max * num), max(num, cur_max, cur_min * num, cur_max * num)
        return cur_max


start_time = time()


# Example 1:
# Input: nums = [3,-1,-5,2,5,-9]
_nums = [3,-1,-5,2,5,-9]
# Output: 1350
# Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
#
# Example 2:
# Input: nums = [-4,-5,-4]
_nums = [-4, -5, -4]
# Output: 20
# Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.

print(Solution().maxStrength(_nums))

print("--- %s seconds ---" % (time() - start_time))
