from time import time


class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) > 1:
            nums = [(nums[i]+nums[i+1])%10 for i in range(len(nums) - 1)]
        return nums[0]


start_time = time()

_nums = [1,2,3,4,5]
# Input: nums = [1,2,3,4,5]
# Output: 8
# Explanation:
# The above diagram depicts the process from which we obtain the triangular sum of the array.

print(Solution().triangularSum(_nums))

print("--- %s seconds ---" % (time() - start_time))
