from time import time


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = 10**5 + 1
        cur_sum = 0
        i = j = 0
        while i < len(nums) and j < len(nums):
            cur_sum += nums[j]
            while cur_sum >= target:
                result = min(result, j - i + 1)
                cur_sum -= nums[i]
                i += 1
            j += 1
        return 0 if result == 10**5 + 1 else result


start_time = time()

_target = 7
_nums = [2, 3, 1, 2, 4, 3]

print(Solution().minSubArrayLen(_target, _nums))

print("--- %s seconds ---" % (time() - start_time))