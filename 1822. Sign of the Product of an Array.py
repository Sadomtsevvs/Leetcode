from time import time


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = True
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign = not sign
        return 1 if sign else -1


start_time = time()

_nums = [-1,-2,-3,-4,3,2,1]
_nums = [-1,1,-1,1,-1]
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1

print(Solution().arraySign(_nums))

print("--- %s seconds ---" % (time() - start_time))
