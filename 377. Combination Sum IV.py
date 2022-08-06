from functools import cache
from time import time
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # official solution
        # 
        nums.sort()

        @cache
        def traverse(remain):
            if remain == 0:
                return 1
            res = 0
            for num in nums:
                if remain < num:
                    break
                res += traverse(remain - num)
            return res

        return traverse(target)

        # official solution
        #
        # # minor optimization
        # # nums.sort()
        # dp = [0 for i in range(target+1)]
        # dp[0] = 1
        #
        # for comb_sum in range(target+1):
        #
        #     for num in nums:
        #         if comb_sum - num >= 0:
        #             dp[comb_sum] += dp[comb_sum-num]
        #         # minor optimization, early stopping.
        #         # else:
        #         #    break
        # return dp[target]



start_time = time()

_nums = [1,2,3]
_target = 4
# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
#
# Example 2:
# Input: nums = [9], target = 3
# Output: 0
_nums = [4,2,1]
_target = 32

_nums = [2,1]
_target = 0

print(Solution().combinationSum4(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))
