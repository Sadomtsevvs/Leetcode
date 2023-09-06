from functools import cache
from time import time
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        @cache
        def dp(i, group):
            if i == len(nums):
                return 0
            num = nums[i]
            result = float('inf')
            if group == 1:
                if num == 1:
                    result = min(result, dp(i + 1, group))
                else:
                    result = min(result, 1 + dp(i + 1, group))
                result = min(result, dp(i, group + 1))
            elif group == 2:
                if num == 2:
                    result = min(result, dp(i + 1, group))
                else:
                    result = min(result, 1 + dp(i + 1, group))
                result = min(result, dp(i, group + 1))
            else:
                if num == 3:
                    result = min(result, dp(i + 1, group))
                else:
                    result = min(result, 1 + dp(i + 1, group))
            return result

        return dp(0, 1)


start_time = time()

# Example 1:
# Input: nums = [2,1,3,2,1]
_nums = [2,1,3,2,1]
# Output: 3
# Explanation: It's optimal to perform three operations:
# 1. change nums[0] to 1.
# 2. change nums[2] to 1.
# 3. change nums[3] to 1.
# After performing the operations and sorting the numbers in each group, group 1 becomes equal to [0,1,2,3,4] and group 2 and group 3 become empty. Hence, res is equal to [0,1,2,3,4] which is sorted in non-decreasing order.
# It can be proven that there is no valid sequence of less than three operations.
#
# Example 2:
# Input: nums = [1,3,2,1,3,3]
# _nums = [1,3,2,1,3,3]
# Output: 2
# Explanation: It's optimal to perform two operations:
# 1. change nums[1] to 1.
# 2. change nums[2] to 1.
# After performing the operations and sorting the numbers in each group, group 1 becomes equal to [0,1,2,3], group 2 becomes empty, and group 3 becomes equal to [4,5]. Hence, res is equal to [0,1,2,3,4,5] which is sorted in non-decreasing order.
# It can be proven that there is no valid sequence of less than two operations.
#
# Example 3:
# Input: nums = [2,2,2,2,3,3]
_nums = [2,2,2,2,3,3]
# Output: 0
# Explanation: It's optimal to not perform operations.

print(Solution().minimumOperations(_nums))

print("--- %s seconds ---" % (time() - start_time))
