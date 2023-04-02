from functools import cache
from time import time


class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:

        # after reading LC comments

        if s1 == s2:
            return True
        if len(s1) == 1:
            return False
        if len(s1) == 2:
            return s1 == s2[::-1]
        if len(s1) == 3:
            return sorted(s1) == sorted(s2)
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
                    or self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False


start_time = time()

# Example 1:
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
# The algorithm stops now, and the result string is "rgeat" which is s2.
# As one possible scenario led s1 to be scrambled to s2, we return true.
#
# Example 2:
_s1 = "abcde"
_s2 = "caebd"
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
#
# Example 3:
# Input: s1 = "a", s2 = "a"
# Output: true


print(Solution().isScramble(_s1, _s2))

print("--- %s seconds ---" % (time() - start_time))
