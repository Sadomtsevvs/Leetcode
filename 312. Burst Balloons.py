from time import time


class Solution:
    def maxCoins(self, nums: list[int]) -> int:


start_time = time()

_nums = [3,1,5,8]
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

print(Solution().maxCoins(_nums))

print("--- %s seconds ---" % (time() - start_time))
