import math
from time import time


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3**round(math.log(n, 3)) == n

        # official solution 1
        # if n < 1:
        #     return False
        # while n % 3 == 0:
        #     n /= 3
        # return n == 1


        # from LC
        # return n > 0 and 3 ** 19 % n == 0



start_time = time()

_n = 27
# Input: n = 27
# Output: true

print(Solution().isPowerOfThree(_n))

print("--- %s seconds ---" % (time() - start_time))
