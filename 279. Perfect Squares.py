from math import sqrt
from time import time


class Solution:
    def numSquares(self, n: int) -> int:
        result = 1
        max_sq = int(sqrt(n))
        cands = [[i, n] for i in range(max_sq, 0, -1)]
        while cands:
            next_cands = []
            for cand, num in cands:
                remain = num - cand**2
                if remain == 0:
                    return result
                max_sq = int(sqrt(remain))
                for i in range(min(max_sq, cand), 0, -1):
                    next_cands.append([i, remain])
            result += 1
            cands = next_cands


start_time = time()

# Example 1:
# Input: n = 12
_n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
_n = 7168

print(Solution().numSquares(_n))

print("--- %s seconds ---" % (time() - start_time))