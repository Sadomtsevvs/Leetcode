from time import time
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # my first O(n**2) solution
        #
        # n = len(nums)
        # if n < 2:
        #     return False
        # if k == 1:
        #     return True
        # for i in range(n-1):
        #     sum = nums[i]
        #     for j in range(i+1, n):
        #         sum += nums[j]
        #         if sum % k == 0:
        #             return True
        # return False

        # official solution
        #
        # initialize the hash map with index 0 for sum 0
        hash_map = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            # if the remainder s % k occurs for the first time
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            # if the subarray size is at least two
            elif hash_map[s % k] < i:
                return True
        return False


start_time = time()

_nums = [23,2,4,6,7]
_k = 6
# Example 1:
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
#
# Example 2:
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
#
# Example 3:
# Input: nums = [23,2,6,4,7], k = 13
# Output: false

print(Solution().checkSubarraySum(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
