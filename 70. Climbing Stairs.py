from time import time


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        res = [0] * (n + 1)
        res[1] = 1
        res[2] = 2
        for i in range(3, n + 1):
            res[i] = res[i-1] + res[i-2]
        return res[n]


start_time = time()

_n = 5

print(Solution().climbStairs(_n))

print("--- %s seconds ---" % (time() - start_time))
