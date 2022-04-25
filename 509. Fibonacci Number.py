from time import time


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev, prev_prev = 1, 0
        for i in range(2, n + 1):
            prev, prev_prev = prev + prev_prev,  prev
        return prev


start_time = time()

_n = 5

print(Solution().fib(_n))

print("--- %s seconds ---" % (time() - start_time))
