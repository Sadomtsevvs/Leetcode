from time import time
from functools import lru_cache


class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:

        # # thanks for idea from LC comments!!!
        #
        # @lru_cache(None)
        # def dp(n, kk):
        #     if n == len(piles):
        #         if kk == 0:
        #             return 0
        #         if kk > 0:
        #             return -float('inf')
        #     ans = dp(n + 1, kk)
        #     sm = 0
        #     for i in range(min(kk, len(piles[n]))):
        #         sm += piles[n][i]
        #         ans = max(ans, sm + dp(n + 1, kk - 1 - i))
        #     return ans
        #
        # return dp(0, k)

        dp = [[0 for __ in range(k+1)] for _ in range(len(piles))]
        dp.append([-float('inf')] * (k+1))
        dp[-1][0] = 0

        for n in range(len(piles) - 1, -1, -1):
            for kk in range(1, k+1):
                ans = dp[n + 1][kk]
                sm = 0
                for i in range(min(kk, len(piles[n]))):
                    sm += piles[n][i]
                    ans = max(ans, sm + dp[n + 1][kk - 1 - i])
                dp[n][kk] = ans

        return dp[0][k]

        # dp = [[0 for __ in range(k)] for _ in range(len(piles))]
        # dp.append([-float('inf')] * (k))
        # dp[-1][0] = 0
        #
        # for n in range(len(piles) - 1, -1, -1):
        #     for kk in range(k):
        #         ans = dp[n + 1][kk]
        #         sm = 0
        #         for i in range(min(kk+1, len(piles[n]))):
        #             sm += piles[n][i]
        #             ans = max(ans, sm + dp[n + 1][kk - i])
        #         dp[n][kk] = ans
        #
        # return dp[0][k-1]

start_time = time()

# _piles = [[1,100,3],[7,8,90]]
# _k = 3
_piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
_k = 7
# Input: piles = [[1,100,3],[7,8,9]], k = 2
# Output: 101
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.

print(Solution().maxValueOfCoins(_piles, _k))

print("--- %s seconds ---" % (time() - start_time))