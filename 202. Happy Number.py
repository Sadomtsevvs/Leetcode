from time import time


class Solution:
    def isHappy(self, n: int) -> bool:
        numbers_passed = set()
        while n not in numbers_passed and n != 1:
            numbers_passed.add(n)
            n = sum([int(x)**2 for x in str(n)])
        return n == 1


start_time = time()

_n = 2
# _n = 19
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

print(Solution().isHappy(_n))

print("--- %s seconds ---" % (time() - start_time))
