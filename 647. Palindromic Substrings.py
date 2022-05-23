from time import time


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 1
        for i in range(1, len(s)):
            res += 1
            for j in range(i):
                mid, add = divmod(i + j, 2)
                if s[j:mid+add] == s[mid+add+1-add:i+1][::-1]:
                    res += 1
        return res

        # from LC comments
        #
        # n = len(s)
        # dp = [[0] * n for _ in range(n)]
        #
        # res = 0
        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         dp[i][j] = s[i] == s[j] and ((j - i + 1) < 3 or dp[i + 1][j - 1])
        #         res += dp[i][j]
        # return res


start_time = time()

_s = "aaa"
_s = "abac"
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

print(Solution().countSubstrings(_s))

print("--- %s seconds ---" % (time() - start_time))
