from functools import cache
from time import time


class Solution:
    def integerBreak(self, n: int) -> int:

        # my solution
        #
        @cache
        def dp(rest):
            if rest < 2:
                return 1
            result = rest
            for i in range(2, rest):
                result = max(result, i * dp(rest - i))
            return result

        if n <= 3:
            return n - 1

        return dp(n)

        #
        # res = [0, 1, 1]
        # for i in range(3, n + 1):
        #     res.append(max([max(res[i - k], (i - k)) * k for k in range(1, i)]))
        # return res[n]

        # solution from LC comments
        #
        # Prod = 1
        # if n > 4:
        #     count = (n - 4) // 3
        #     n = n - 3 * count
        #     Prod *= 3 ** count
        # if n == 6:
        #     Prod *= 9
        # elif n == 5:
        #     Prod *= 6
        # elif n == 4:
        #     Prod *= 4
        # elif n == 3:
        #     Prod *= 2
        # return Prod

start_time = time()

_n = 58
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

print(Solution().integerBreak(_n))

print("--- %s seconds ---" % (time() - start_time))
