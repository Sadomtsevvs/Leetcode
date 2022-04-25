from time import time


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            mid2 = mid * mid
            if mid2 == num:
                return True
            if mid2 < num:
                l = mid + 1
            else:
                r = mid - 1
        return False


start_time = time()

_num = 14
# Input: num = 16
# Output: true

print(Solution().isPerfectSquare(_num))

print("--- %s seconds ---" % (time() - start_time))
