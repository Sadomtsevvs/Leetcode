from functools import lru_cache
from time import time


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @lru_cache()
        def dp(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            if s[i] == t[j]:
                return dp(i + 1, j + 1)
            else:
                return dp(i, j + 1)
        return dp(0, 0)

        # Babichev, 2 pointers
        #
        # s_i, t_i = 0, 0
        # while s_i < len(s) and t_i < len(t):
        #     s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1
        # return s_i == len(s)

        # Pochmann
        #
        # remainder_of_t = iter(t)
        # for letter in s:
        #     if letter not in remainder_of_t:
        #         return False
        # return True


start_time = time()

_s = "abc"
_t = "ahbgdc"
_s = "axc"
_t = "ahbgdc"
# Input: s = "abc", t = "ahbgdc"
# Output: true

print(Solution().isSubsequence(_s, _t))

print("--- %s seconds ---" % (time() - start_time))