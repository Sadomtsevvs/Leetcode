from time import time


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # bottom up solution
        #
        n = len(text1)
        m = len(text2)
        res = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    res[i][j] = 1 + res[i-1][j-1]
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1])
        return res[n][m]

        # top-down solution
        #
        # @cache
        # def dp(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + dp(i+1, j+1)
        #     else:
        #         return max(dp(i, j+1), dp(i+1, j))
        #
        # return dp(0, 0)


start_time = time()

_text1 = "abcde"
_text2 = "abec"
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

print(Solution().longestCommonSubsequence(_text1, _text2))

print("--- %s seconds ---" % (time() - start_time))
