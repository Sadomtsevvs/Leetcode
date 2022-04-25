from time import time
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dp(i1, i2, i3):
            if i3 == len(s3):
                if i1 == len(s1) and i2 == len(s2):
                    return True
                return False
            if i1 < len(s1) and s3[i3] == s1[i1] and i2 < len(s2) and s3[i3] == s2[i2]:
                return dp(i1+1, i2, i3+1) or dp(i1, i2+1, i3+1)
            if i1 < len(s1) and s3[i3] == s1[i1]:
                return dp(i1+1, i2, i3+1)
            if i2 < len(s2) and s3[i3] == s2[i2]:
                return dp(i1, i2+1, i3+1)
            return False

        return dp(0, 0, 0)

        # from official solution: i can use only 2 states, because i3 = i1 + i2


start_time = time()

_s1 = "aabcc"
_s2 = "dbbca"
_s3 = "aadbbcbcac"
# _s1 = "aabcc"
# _s2 = "dbbca"
# _s3 = "aadbbbaccc"
# _s1 = ""
# _s2 = ""
# _s3 = ""
_s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
_s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
_s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

print(Solution().isInterleave(_s1, _s2, _s3))

print("--- %s seconds ---" % (time() - start_time))