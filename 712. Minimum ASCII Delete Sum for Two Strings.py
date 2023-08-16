from functools import cache
from time import time


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @cache
        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return 0
            if i1 == len(s1):
                return dfs(i1, i2 + 1) + ord(s2[i2])
            if i2 == len(s2):
                return dfs(i1 + 1, i2) + ord(s1[i1])
            if s1[i1] == s2[i2]:
                return dfs(i1 + 1, i2 + 1)
            return min(dfs(i1, i2 + 1) + ord(s2[i2]), dfs(i1 + 1, i2) + ord(s1[i1]))

        return dfs(0, 0)


start_time = time()

# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
#
# Example 2:
# Input: s1 = "delete", s2 = "leet"
_s1 = "delete"
_s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

print(Solution().minimumDeleteSum(_s1, _s2))

print("--- %s seconds ---" % (time() - start_time))
