from time import time


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        # I can't solve this problem

        # official solution, approach 5
        #
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        M = 10 ** 9 + 7
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    a = dp[i - 1][j - i] if j >= i else 0
                    val = (dp[i - 1][j] + M - a) % M
                    dp[i][j] = (dp[i][j - 1] + val) % M
        a = dp[n][k - 1] if k > 0 else 0
        return (dp[n][k] + M - a) % M

        # solution from Babichev
        #
        # dp = [[1] * (k + 1) for _ in range(n + 1)]
        # sp = [[1] * (k + 1) for _ in range(n + 1)]
        # N = 10 ** 9 + 7
        # for i in range(1, n + 1):
        #     for j in range(1, k + 1):
        #         dp[i][j] = sp[i - 1][j] if j < i else (sp[i - 1][j] - sp[i - 1][j - i]) % N
        #         sp[i][j] = (sp[i][j - 1] + dp[i][j]) % N
        # return dp[-1][-1]


start_time = time()

_n = 3
_k = 0
# Example 1:
# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
#
# Example 2:
# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

print(Solution().kInversePairs(_n, _k))

print("--- %s seconds ---" % (time() - start_time))
