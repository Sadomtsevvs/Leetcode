from time import time


class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        if n == 0:
            return first
        elif n == 1:
            return second
        for i in range(3, n + 1):
            third, second, first = first + second + third, third, second
        return third


start_time = time()

_n = 25
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

print(Solution().tribonacci(_n))

print("--- %s seconds ---" % (time() - start_time))
