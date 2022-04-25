from time import time


class Solution:
    def rob(self, nums: list[int]) -> int:

        n = len(nums)
        classic = [0] * n
        middle = [0] * n

        classic[0] = nums[0]
        middle[0] = 0
        if n == 1:
            return classic[0]
        classic[1] = max(nums[0], nums[1])
        middle[1] = 0
        if n == 2:
            return classic[1]
        classic[2] = max(nums[0] + nums[2], nums[1])
        middle[2] = nums[1]

        if n > 3:
            middle[3] = max(nums[1], nums[2])
        if n > 4:
            middle[4] = max(nums[1] + nums[3], nums[2])

        for i in range(3, n):
            classic[i] = max(classic[i - 1], classic[i - 2] + nums[i], classic[i - 3] + nums[i])
        for i in range(5, n):
            middle[i] = max(middle[i - 1], middle[i - 2] + nums[i - 1], middle[i - 3] + nums[i - 1])

        return max(classic[n - 2], nums[n - 1] + middle[n - 2])

        # another good explain https://leetcode.com/problems/house-robber-ii/discuss/299071/Python-O(n)-time-O(1)-space

start_time = time()

_nums = [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]
# 41
# _nums = [2,3,2]

print(Solution().rob(_nums))

print("--- %s seconds ---" % (time() - start_time))
