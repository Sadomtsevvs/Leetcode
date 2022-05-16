from time import time


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        while z > 0:
            if z % 2 == 1:
                ans += 1
            z >>= 1
        return ans


start_time = time()

_x = 1
_y = 2
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

print(Solution().hammingDistance(_x, _y))

print("--- %s seconds ---" % (time() - start_time))