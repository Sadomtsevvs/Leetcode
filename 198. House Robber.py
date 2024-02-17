from time import time


class Solution:
    def rob(self, nums: list[int]) -> int:

        # space optimized iterative solution
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        prev_2 = nums[0]
        prev_1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev_2, prev_1 = prev_1, max(prev_1, nums[i] + prev_2)
        return prev_1

        # iterative solution
        #
        # result = [0] * len(nums)
        # result[0] = nums[0]
        # if len(nums) == 1:
        #     return result[0]
        # result[1] = max(nums[0], nums[1])
        # if len(nums) == 2:
        #     return result[1]
        # for i in range(3, len(nums)):
        #     result[i] = max(result[i-1], result[i-2] + nums[i])
        # return result[-1]

        # top-down solution
        #
        # @cache
        # def dp(i, previous_robbbed):
        #     if i >= len(nums):
        #         return 0
        #     result = dp(i+1, False)
        #     if not previous_robbbed:
        #         result = max(result, nums[i] + dp(i+1, True))
        #     return result


start_time = time()

_nums = [2, 7, 9, 3, 1]

print(Solution().rob(_nums))

print("--- %s seconds ---" % (time() - start_time))
