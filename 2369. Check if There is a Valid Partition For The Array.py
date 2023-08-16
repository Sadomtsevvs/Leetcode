from time import time
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        dp = [False] * (len(nums) + 1)
        dp[0] = True

        for i in range(2, len(nums) + 1):
            dp[i] = dp[i - 2] and (nums[i - 2] == nums[i - 1])
            if i > 2:
                dp[i] = dp[i] or (dp[i - 3] and (nums[i - 3] == nums[i - 2] == nums[i - 1]))
                dp[i] = dp[i] or (dp[i - 3] and (nums[i - 3] + 2 == nums[i - 2] + 1 == nums[i - 1]))

        return dp[-1]


start_time = time()

# Example 1:
# Input: nums = [4,4,4,5,6]
_nums = [4,4,4,5,6]
# Output: true
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.
#
# Example 2:
# Input: nums = [1,1,1,2]
# Output: false
# Explanation: There is no valid partition for this array.

print(Solution().validPartition(_nums))

print("--- %s seconds ---" % (time() - start_time))
