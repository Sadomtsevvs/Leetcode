from time import time
from math import log, log2


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = log2(n)
        return True if x == int(x) else False


start_time = time()

# _n = 536870912
_n = 0

print(Solution().isPowerOfTwo(_n))

print("--- %s seconds ---" % (time() - start_time))