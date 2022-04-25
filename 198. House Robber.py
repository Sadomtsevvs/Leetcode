from time import time


class Solution:
    def rob(self, nums: list[int]) -> int:
        result = [0] * len(nums)
        result[0] = nums[0]
        if len(nums) == 1:
            return result[0]
        result[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return result[1]
        for i in range(3, len(nums)):
            result[i] = max(result[i-1], result[i-2] + nums[i])
        return result[-1]

start_time = time()

_nums = [2, 7, 9, 3, 1]

print(Solution().rob(_nums))

print("--- %s seconds ---" % (time() - start_time))
