from functools import cache
from time import time
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        @cache
        def dp(i, covered):
            if i > n:
                if len(covered) == n + 1:
                    return 0
                else:
                    return float('inf')
            # don't open
            result = dp(i + 1, covered)
            # open
            tap = ranges[i]
            if tap != 0:
                tap_covered = set(j for j in range(i - tap, i + tap + 1) if 0 <= j <= n)
                set_covered = set(covered) | tap_covered
                total_covered = list(set_covered)
                total_covered.sort()
                result = min(result, 1 + dp(i + 1, tuple(total_covered)))

            return result

        res = dp(0, tuple())
        return -1 if res == float('inf') else res


start_time = time()

# Example 1:
# Input: n = 5, ranges = [3,4,1,1,0,0]
_n = 5
_ranges = [3,4,1,1,0,0]
# Output: 1
# Explanation: The tap at point 0 can cover the interval [-3,3]
# The tap at point 1 can cover the interval [-3,5]
# The tap at point 2 can cover the interval [1,3]
# The tap at point 3 can cover the interval [2,4]
# The tap at point 4 can cover the interval [4,4]
# The tap at point 5 can cover the interval [5,5]
# Opening Only the second tap will water the whole garden [0,5]
#
# Example 2:
# Input: n = 3, ranges = [0,0,0,0]
# Output: -1
# Explanation: Even if you activate all the four taps you cannot water the whole garden.

_n = 35
_ranges = [1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]

print(Solution().minTaps(_n, _ranges))

print("--- %s seconds ---" % (time() - start_time))
