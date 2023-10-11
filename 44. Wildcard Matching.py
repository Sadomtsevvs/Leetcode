from functools import cache
from time import time


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dp(ind_s, ind_p):
            if ind_s == len(s) and ind_p == len(p):
                return True
            if ind_s > len(s):
                return False
            if ind_p == len(p):
                return False
            result = False
            if p[ind_p] == '*':
                result |= dp(ind_s + 1, ind_p + 1) or dp(ind_s + 1, ind_p) or dp(ind_s, ind_p + 1)
            if ind_s < len(s) and (s[ind_s] == p[ind_p] or p[ind_p] == '?'):
                result |= dp(ind_s + 1, ind_p + 1)
            return result

        return dp(0, 0)


start_time = time()

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
# Example 2:
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
# Example 3:
# Input: s = "cb", p = "?a"
_s = "aa"
_p = "aa"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# _s = ""
# _p = "****"

print(Solution().isMatch(_s, _p))

print("--- %s seconds ---" % (time() - start_time))
