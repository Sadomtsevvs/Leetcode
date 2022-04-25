from time import time


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def ppow(xx, nn):
            if nn == 0:
                return 1
            if nn == 1:
                return xx
            half = ppow(xx, nn // 2)
            if nn % 2 == 0:
                return half * half
            return half * half * x

        if n < 0:
            x, n = 1/x, -n

        return ppow(x, n)

        # def ppow(xx, nn):
        #     if nn == 0:
        #         return 1
        #     if nn == 1:
        #         return xx
        #     if nn % 2 == 0:
        #         return ppow(xx, nn // 2) ** 2
        #     return ppow(xx, nn // 2) ** 2 * x
        #
        # if n < 0:
        #     x, n = 1/x, -n
        #
        # return ppow(x, n)

start_time = time()

_x = 2.00000
_n = 10
# _x = 2.00000
# _n = -2
_x = 0.00001
_n = 2147483647

# Input: x = 2.00000, n = 10
# Output: 1024.00000

print(Solution().myPow(_x, _n))

print("--- %s seconds ---" % (time() - start_time))
