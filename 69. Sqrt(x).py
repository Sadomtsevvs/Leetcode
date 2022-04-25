from time import time


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            m = (l + r) // 2
            m2 = m ** 2
            if m2 == x:
                return m
            if m2 > x:
                r = m - 1
            else:
                l = m + 1
        return l - 1


start_time = time()

_x = 1
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

print(Solution().mySqrt(_x))

print("--- %s seconds ---" % (time() - start_time))
