from time import time


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_ind = 0
        for i in range(len(nums)):
            if max_ind < i:
                return False
            max_ind = max(max_ind, i + nums[i])
        return True

start_time = time()

_nums = [2, 3, 1, 1, 4]
# Output: true
# _nums = [3, 2, 1, 0, 4]
# Output: false

print(Solution().canJump(_nums))

print("--- %s seconds ---" % (time() - start_time))
