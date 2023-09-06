from functools import cache
from time import time


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        if len(str2) > len(str1):
            return False

        # @cache
        # def dp(i, j):
        #     if i == len(str1):
        #         if j == len(str2):
        #             return True
        #         else:
        #             return False
        #     if j == len(str2):
        #         return True
        #     char1, char2 = ord(str1[i]), ord(str2[j])
        #     return (char1 == char2 or char1 + 1 == char2 or char1 - char2 == 25) and dp(i + 1, j + 1) or dp(i + 1, j)
        #
        # return dp(0, 0)

        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            char1, char2 = ord(str1[i]), ord(str2[j])
            if char1 == char2 or char1 + 1 == char2 or char1 - char2 == 25:
                i += 1
                j += 1
            else:
                i += 1

        return j == len(str2)


start_time = time()

# Example 1:
# Input: str1 = "abc", str2 = "ad"
# Output: true
# Explanation: Select index 2 in str1.
# Increment str1[2] to become 'd'.
# Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.
#
# Example 2:
# Input: str1 = "zc", str2 = "ad"
_str1 = "zc"
_str2 = "ad"
# Output: true
# Explanation: Select indices 0 and 1 in str1.
# Increment str1[0] to become 'a'.
# Increment str1[1] to become 'd'.
# Hence, str1 becomes "ad" and str2 is now a subsequence. Therefore, true is returned.
#
# Example 3:
# Input: str1 = "ab", str2 = "d"
_str1 = "ab"
_str2 = "d"
# Output: false
# Explanation: In this example, it can be shown that it is impossible to make str2 a subsequence of str1 using the operation at most once.
# Therefore, false is returned.

# _str1 = "dm"
# _str2 = "e"

print(Solution().canMakeSubsequence(_str1, _str2))

print("--- %s seconds ---" % (time() - start_time))
