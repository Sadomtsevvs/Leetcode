from time import time
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        # too slow
        #
        # result = 0
        # def dp(remain, cursum):
        #     nonlocal result
        #     if cursum > target:
        #         return
        #     if remain == 0 and cursum == target:
        #         result += 1
        #         return
        #     for num in range(1, k + 1):
        #         dp(remain - 1, cursum + num)
        #
        # dp(n, 0)
        # return result % (10**9 + 7)

        # bottom-up, work normal
        #
        result = [[0 for _ in range(target)] for _ in range(n)]
        for num in range(k):
            if num < target:
                result[0][num] = 1
        for i in range(1, n):
            for j in range(i, (i+1)*k):
                if j >= target:
                    break
                for num in range(k):
                    if j-num-1 >= 0:
                        result[i][j] += result[i-1][j-num-1]
        return result[n-1][target-1] % (10**9 + 7)

        # top-down, work fast
        #
        # @cache
        # def dp(remain, cursum):
        #     if cursum <= 0 or cursum > remain*k:
        #         return 0
        #     if remain == 1 and cursum <= k:
        #         return 1
        #     return sum([dp(remain - 1, cursum - num) for num in range(1, k + 1)])
        #
        # return dp(n, target) % (10**9 + 7)

start_time = time()

_n = 1
_k = 6
_target = 3
_n = 2
_k = 6
_target = 7
_n = 30
_k = 30
_target = 500
# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

print(Solution().numRollsToTarget(_n, _k, _target))

print("--- %s seconds ---" % (time() - start_time))
