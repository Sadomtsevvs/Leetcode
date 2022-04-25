from time import time


class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 != 0:
            return []
        n = num // 3
        return [n - 1, n, n + 1]


start_time = time()

_num = 33
# Input: num = 33
# Output: [10,11,12]
# Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
# 10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].

print(Solution().sumOfThree(_num))

print("--- %s seconds ---" % (time() - start_time))
