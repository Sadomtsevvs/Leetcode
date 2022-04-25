from time import time


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        result = 0
        for i in range(len(nums)-1):
            nums_i = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == nums_i and (i * j) % k == 0:
                    result += 1
        return result


start_time = time()

_nums = [3,1,2,2,2,1,3]
_k = 2
_nums = [1,2,3,4]
_k = 1
# Input: nums = [3,1,2,2,2,1,3], k = 2
# Output: 4
# Explanation:
# There are 4 pairs that meet all the requirements:
# - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
# - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
# - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
# - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

print(Solution().countPairs(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
