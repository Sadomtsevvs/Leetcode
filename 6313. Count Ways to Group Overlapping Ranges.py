from time import time
from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        groups = 1
        beg, end = ranges[0]
        for i in range(1, len(ranges)):
            r = ranges[i]
            if end >= r[0]:
                end = max(end, r[1])
            else:
                groups += 1
                beg, end = r
        return 2**groups % (10**9 + 7)


start_time = time()

_ranges = [[6,10],[5,15]]
# Example 1:
# Input: ranges = [[6,10],[5,15]]
# Output: 2
# Explanation:
# The two ranges are overlapping, so they must be in the same group.
# Thus, there are two possible ways:
# - Put both the ranges together in group 1.
# - Put both the ranges together in group 2.
#
_ranges = [[1,3],[10,20],[2,5],[4,8]]
# Example 2:
# Input: ranges = [[1,3],[10,20],[2,5],[4,8]]
# Output: 4
# Explanation:
# Ranges [1,3], and [2,5] are overlapping. So, they must be in the same group.
# Again, ranges [2,5] and [4,8] are also overlapping. So, they must also be in the same group.
# Thus, there are four possible ways to group them:
# - All the ranges in group 1.
# - All the ranges in group 2.
# - Ranges [1,3], [2,5], and [4,8] in group 1 and [10,20] in group 2.
# - Ranges [1,3], [2,5], and [4,8] in group 2 and [10,20] in group 1.

_ranges = [[3,10],[15,19],[22,28],[34,40],[54,54],[55,56],[77,77],[77,88],[97,98],[2,7]]

print(Solution().countWays(_ranges))

print("--- %s seconds ---" % (time() - start_time))
