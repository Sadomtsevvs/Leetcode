from functools import cache
from time import time


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        # @cache
        # def dp(i):
        #     if i < 0:
        #         return 0
        #     # if i == len(s) - 1:
        #     #     if int(s[-1]) > k:
        #     #         return 0
        #     #     else:
        #     #         return 1
        #     if s[i] == '0':
        #         return 0
        #     mult = 1
        #     m = min(len(str(k)), len(s) - i)
        #     if int(s[i:i + m]) <= k:
        #         mult *= 2
        #     return mult * dp(i + 1)
        #
        # return dp(len(s)-1)

        @cache
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            count = 0
            for j in range(i, len(s)):
                if int(s[i:j+1]) > k:
                    break
                count += dp(j+1)
            return count % (10**9 + 7)

        return dp(0)


start_time = time()

# Example 1:
# Input: s = "1000", k = 10000
_s = "1000"
_k = 10000
# Output: 1
# Explanation: The only possible array is [1000]
#
# Example 2:
# Input: s = "1000", k = 10
# _s = "1000"
# _k = 10
# Output: 0
# Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
#
# Example 3:
# Input: s = "1317", k = 2000
# _s = "1317"
# _k = 2000
# Output: 8
# Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

print(Solution().numberOfArrays(_s, _k))

print("--- %s seconds ---" % (time() - start_time))
