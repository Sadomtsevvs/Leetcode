from functools import cache
from time import time
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(i, cur_sum):
            if i == len(nums):
                return int(cur_sum == target)
            return dfs(i + 1, cur_sum + nums[i]) + dfs(i + 1, cur_sum - nums[i])

        return dfs(0, 0)


start_time = time()

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
_nums = [1,1,1,1,1]
_target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
# Example 2:
# Input: nums = [1], target = 1
# Output: 1

print(Solution().findTargetSumWays(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))
