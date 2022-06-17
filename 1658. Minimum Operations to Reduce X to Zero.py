from time import time
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        # LC hint: find the maximum subarray greedily
        if sum(nums) < x:
            return -1
        elif sum(nums) == x:
            return len(nums)

        target = sum(nums) - x
        max_len = 0
        beg = 0
        for i in range(len(nums)):
            while beg < i and target - nums[i] < 0:
                target += nums[beg]
                beg += 1
            target -= nums[i]
            if target == 0:
                max_len = max(max_len, i - beg + 1)

        return -1 if max_len == 0 else len(nums) - max_len


        # dp: TLE, MLE
        #
        # if sum(nums) < x:
        #     return -1
        #
        # @lru_cache(None)
        # def dp(left, right, remain):
        #     if remain == 0:
        #         return 0
        #     if left > right or remain < 0:
        #         return float('inf')
        #     return 1 + min(dp(left + 1, right, remain - nums[left]), dp(left, right - 1, remain - nums[right]))
        #
        # result = dp(0, len(nums) - 1, x)
        # return -1 if result == float('inf') else result




start_time = time()

_nums = [3,2,20,1,1,3]
_x = 10
_nums = [1,1,4,2,3]
_x = 5
_nums = [5,6,7,8,9]
_x = 4
_nums = [1,2,3,4,5]
_x = 15
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

print(Solution().minOperations(_nums, _x))

print("--- %s seconds ---" % (time() - start_time))
