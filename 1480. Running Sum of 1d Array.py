from itertools import accumulate
from time import time
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)


start_time = time()

_nums = [1,2,3,4]
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

print(Solution().runningSum(_nums))

print("--- %s seconds ---" % (time() - start_time))
