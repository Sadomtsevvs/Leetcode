import math
from time import time


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        left, right = 0, int(n**0.3)
        while left <= right:
            mid = (right + left) // 2
            power = 4 ** mid
            if power == n:
                return True
            elif power < n:
                left = mid + 1
            else:
                right = mid - 1
        return False

        # from Babichev
        #
        # return num > 0 and num & (num - 1) == 0 and 0b1010101010101010101010101010101 & num == num


start_time = time()

_n = 387420489
_n = 64
# Input: n = 16
# Output: true

print(Solution().isPowerOfFour(_n))

print("--- %s seconds ---" % (time() - start_time))
