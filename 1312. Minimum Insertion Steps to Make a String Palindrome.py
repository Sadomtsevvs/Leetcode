from functools import cache
from time import time


class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def dp(beg, end):
            if end - beg < 1:
                return 0
            if s[beg] == s[end]:
                return dp(beg + 1, end - 1)
            else:
                return 1 + min(dp(beg, end-1), dp(beg+1, end))

        return dp(0, len(s) - 1)


start_time = time()

# Example 1:
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
#
# Example 2:
# Input: s = "mbadm"
_s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
#
# Example 3:
# Input: s = "leetcode"
_s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".

print(Solution().minInsertions(_s))

print("--- %s seconds ---" % (time() - start_time))
