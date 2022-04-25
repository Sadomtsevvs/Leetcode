from time import time


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxres = 0
        res = 0
        for i in nums:
            if i == 1:
                res += 1
            else:
                maxres = max(maxres, res)
                res = 0
        return max(maxres, res)


start_time = time()

_nums = [1, 1, 0, 1, 1, 1]

print(Solution().findMaxConsecutiveOnes(_nums))

print("--- %s seconds ---" % (time() - start_time))
