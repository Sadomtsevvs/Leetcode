from time import time
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left = n
        cur_zeroes = 1
        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 1:
        for plot in flowerbed:
            if plot == 1:
                left -= (cur_zeroes-1) // 2
                if left == 0:
                    return True
                cur_zeroes = 0
            else:
                cur_zeroes += 1
        left -= cur_zeroes // 2
        return left <= 0


start_time = time()

# Example 1:
# Input: flowerbed = [1,0,0,0,1]
# n = 1
# Output: true
#
# Example 2:
# Input: flowerbed = [1,0,0,0,1]
# n = 2
# Output: false
_flowerbed = [1,0,0,0,1]
_n = 2

_flowerbed = [0,0,1,0,0,0,1,0]
_n = 2

print(Solution().canPlaceFlowers(_flowerbed, _n))

print("--- %s seconds ---" % (time() - start_time))
