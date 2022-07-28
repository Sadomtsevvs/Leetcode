from time import time


class Solution:
    def numWays(self, n: int, k: int) -> int:
        # after reading official solution
        #
        dp = [0 for _ in range(n)]
        dp[0] = k
        if n > 1:
            dp[1] = dp[0] * k
        for i in range(2, n):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])
        return dp[-1]

        # from LC, great
        #
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return k
        # same, dif = k, k * (k - 1)
        # for i in range(3, n + 1):
        #     same, dif = dif, (same + dif) * (k - 1)
        # return same + dif


start_time = time()

_n = 3
_k = 2
# Example 1:
# Input: n = 3, k = 2
# Output: 6
# Explanation: All the possibilities are shown.
# Note that painting all the posts red or all the posts green is invalid
# because there cannot be three posts in a row with the same color.
#
# Example 2:
# Input: n = 1, k = 1
# Output: 1
#
_n = 7
_k = 2
# Example 3:
# Input: n = 7, k = 2
# Output: 42

print(Solution().numWays(_n, _k))

print("--- %s seconds ---" % (time() - start_time))
