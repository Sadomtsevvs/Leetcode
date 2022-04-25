from time import time
from functools import cache


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:

        # top-down
        @cache
        def dp(i, n):
            if n < 0:
                return float('inf')
            if i < 0:
                return 0
            return min(dp(i-carpetLen,n-1), dp(i-1,n) + int(floor[i]))

        return dp(len(floor)-1, numCarpets)

        # bottom-up solution, doesn't work correct
        # dp = [[0 for _ in range(numCarpets + 1)] for __ in range(len(floor)+carpetLen)]
        # for i in range(len(floor)+carpetLen):
        #     dp[i][0] = 1001
        #
        # for i in range(carpetLen, len(floor) + carpetLen):
        #     for n in range(1, numCarpets + 1):
        #         dp[i][n] = min(dp[i-carpetLen][n-1], dp[i-1][n] + int(floor[i-carpetLen]))
        #
        # return dp[len(floor)+carpetLen-1][numCarpets]


start_time = time()

_floor = "10110101"
_numCarpets = 2
_carpetLen = 2
# Input: floor = "10110101", numCarpets = 2, carpetLen = 2
# Output: 2
# Explanation:
# The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
# No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.

print(Solution().minimumWhiteTiles(_floor, _numCarpets, _carpetLen))

print("--- %s seconds ---" % (time() - start_time))