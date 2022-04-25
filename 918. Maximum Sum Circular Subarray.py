from time import time


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        # brute force, too slow
        #
        # best = -float('inf')
        # for i in range(len(nums)):
        #     curr = -float('inf')
        #     for num in (nums[i:] + nums[:i]):
        #         curr = max(curr + num, num)
        #         best = max(best, curr)
        # return best

        # solution from best comment
        #
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
            total += num
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum

start_time = time()

_nums = [-2,4,-5,4,-5,9,4]
# _nums = [5, -3, 5]
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

print(Solution().maxSubarraySumCircular(_nums))

print("--- %s seconds ---" % (time() - start_time))
