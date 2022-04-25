from time import time


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            g = guess(m)
            if g == 0:
                return m
            if g == -1:
                r = m - 1
            else:
                l = m + 1


start_time = time()

_n = 10
# Input: n = 10, pick = 6
# Output: 6

print(Solution().guessNumber(_n))

print("--- %s seconds ---" % (time() - start_time))
