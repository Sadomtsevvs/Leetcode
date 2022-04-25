from time import time


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        # my first solution, i don't like it, but it works

        result = cur_sum = nums[0]
        first = 0
        for last in range(1, len(nums)):
            if cur_sum <= 0 and nums[last] > 0:
                first = last
                cur_sum = nums[last]
            elif nums[first] < 0 and nums[last] > nums[first]:
                while nums[last] > nums[first]:
                    cur_sum -= nums[first]
                    first += 1
                cur_sum += nums[last]
            else:
                cur_sum += nums[last]
            result = max(result, cur_sum)
        return result

        # solution from LC comments 1
        #
        # local_best = float('-inf')
        # global_best = float('-inf')
        # for n in nums:
        #     local_best = max(local_best + n, n)
        #     global_best = max(global_best, local_best)
        # return global_best

        # solution from LC comments 2
        #
        # dp = [*nums]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        # return max(dp)

        # solution from LC comments 3
        #
        # cur_max, max_till_now = 0, -inf
        # for c in nums:
        #     cur_max = max(c, cur_max + c)
        #     max_till_now = max(max_till_now, cur_max)
        # return max_till_now

start_time = time()

# _nums = [-2,-3,1]
# _nums = [5,4,-1,7,8]
_nums = [-2,1,-3,4,-1,2,1,-5,4]
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

print(Solution().maxSubArray(_nums))

print("--- %s seconds ---" % (time() - start_time))
