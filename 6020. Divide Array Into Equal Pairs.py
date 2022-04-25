from time import time
from collections import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        for v in Counter(nums).values():
            if v % 2 != 0:
                return False
        return True


start_time = time()

_nums = [3,2,3,2,2,2]
_nums = [1,2,3,4]
# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation:
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

print(Solution().divideArray(_nums))

print("--- %s seconds ---" % (time() - start_time))