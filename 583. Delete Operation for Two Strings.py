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


start_time = time()

_word1 = "leetcode"
_word2 = "etco"
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

print(Solution().minDistance(_word1, _word2))

print("--- %s seconds ---" % (time() - start_time))
