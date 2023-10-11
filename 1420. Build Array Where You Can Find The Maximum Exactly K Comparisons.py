from functools import cache
from time import time


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        mod = 10 ** 9 + 7

        @cache
        def dp(remain, cur_k, cur_max):
            if cur_k > k:
                return 0
            if remain == 0:
                if cur_k == k:
                    return 1
                else:
                    return 0
            # combs = 0
            # for i in range(1, m + 1):
            #     if i > cur_max:
            #         combs += dp(remain-1, cur_k+1, i)
            #     else:
            #         combs += dp(remain-1, cur_k, cur_max)
            combs = cur_max * dp(remain - 1, cur_k, cur_max)
            for i in range(cur_max + 1, m + 1):
                combs += dp(remain - 1, cur_k + 1, i)
            return combs % mod

        return dp(n, 0, 0)


start_time = time()

# Example 1:
# Input: n = 2, m = 3, k = 1
_n = 2
_m = 3
_k = 1
# Output: 6
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
#
# Example 2:
# Input: n = 5, m = 2, k = 3
# Output: 0
# Explanation: There are no possible arrays that satisify the mentioned conditions.
#
# Example 3:
# Input: n = 9, m = 1, k = 1
# Output: 1
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

print(Solution().numOfArrays(_n, _m, _k))

print("--- %s seconds ---" % (time() - start_time))
