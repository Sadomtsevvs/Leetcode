from time import time
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # my second solution without one list
        #
        n = len(nums)
        from_right_to_left = [0 for _ in range(n + 2)]
        sum_right = 0
        for i in range(n):
            sum_right += nums[n - 1 - i]
            from_right_to_left[n - i] = sum_right
        sum_left = 0
        for i in range(n):
            if sum_left == from_right_to_left[i + 2]:
                return i
            sum_left += nums[i]
        return -1

        # my first solution
        #
        # n = len(nums)
        # from_left_to_right = [0 for _ in range(n+2)]
        # from_right_to_left = [0 for _ in range(n+2)]
        # sum_left, sum_right = 0, 0
        # for i in range(n):
        #     sum_left += nums[i]
        #     sum_right += nums[n-1-i]
        #     from_left_to_right[i+1] = sum_left
        #     from_right_to_left[n-i] = sum_right
        # for i in range(n):
        #     if from_left_to_right[i] == from_right_to_left[i+2]:
        #         return i
        # return -1


start_time = time()

_nums = [1,7,3,6,5,6]
# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
#
# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#
# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

print(Solution().pivotIndex(_nums))

print("--- %s seconds ---" % (time() - start_time))
