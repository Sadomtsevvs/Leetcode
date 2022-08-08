import math
from time import time


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets) / math.log(minutesToTest // minutesToDie + 1))

        # solution from Pochmann
        #
        # pigs = 0
        # while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        #     pigs += 1
        # return pigs


start_time = time()

_buckets = 1000
_minutesToDie = 15
_minutesToTest = 60
# Example 1:
# Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
# Output: 5
#
# Example 2:
# Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
# Output: 2
#
# Example 3:
# Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
# Output: 2

print(Solution().poorPigs(_buckets, _minutesToDie, _minutesToTest))

print("--- %s seconds ---" % (time() - start_time))
