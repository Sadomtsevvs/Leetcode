from functools import cache
from time import time


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        # after reading comments
        #
        @cache
        def dp(i, prev, prev_cnt, k):
            if k < 0:
                return float('inf')
            if i == len(s):
                return 0
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            if s[i] == prev:
                not_delete = dp(i + 1, s[i], prev_cnt + 1, k)
                if prev_cnt in {1, 9, 99}:
                    not_delete += 1
            else:
                not_delete = 1 + dp(i + 1, s[i], 1, k)
            return min(delete, not_delete)

        return dp(0, '', 0, k)


start_time = time()

_s = "aaabcccd"
_k = 2
# Example 1:
# Input: s = "aaabcccd", k = 2
# Output: 4
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
#
# Example 2:
# Input: s = "aabbaa", k = 2
# Output: 2
# Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
#
# Example 3:
# Input: s = "aaaaaaaaaaa", k = 0
# Output: 3
# Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.

print(Solution().getLengthOfOptimalCompression(_s, _k))

print("--- %s seconds ---" % (time() - start_time))
