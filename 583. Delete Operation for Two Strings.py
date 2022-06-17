from time import time


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # solution is looked from Khiryanov lecture
        n = len(word1)
        m = len(word2)
        res = [[i + j if i == 0 or j == 0 else 0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j] = 1 + min(res[i-1][j], res[i][j-1])
        return res[n][m]

        # my second solution
        # @cache
        # def dp(ind1, ind2):
        #     if ind1 == len(word1):
        #         return len(word2) - ind2
        #     elif ind2 == len(word2):
        #         return len(word1) - ind1
        #     elif word1[ind1] == word2[ind2]:
        #         return dp(ind1 + 1, ind2 + 1)
        #     else:
        #         return 1 + min(dp(ind1 + 1, ind2), dp(ind1, ind2 + 1))
        #
        # return dp(0, 0)

        # from Lee
        #
        # m, n = len(w1), len(w2)
        # dp = [[0] * (n + 1) for i in range(m + 1)]
        # for i in range(m):
        #     for j in range(n):
        #         dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
        # return m + n - 2 * dp[m][n]



start_time = time()

_word1 = "leetcode"
_word2 = "etco"
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

print(Solution().minDistance(_word1, _word2))

print("--- %s seconds ---" % (time() - start_time))
