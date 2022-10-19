from functools import cache
from time import time


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:

        @cache
        def dp(i, cur_max, remain):
            if remain == 0:
                return float('inf')
            if len(jobDifficulty) - i < remain:
                return float('inf')
            if i == len(jobDifficulty) - 1:
                return cur_max
            include = dp(i+1, max(cur_max, jobDifficulty[i+1]), remain)
            not_include = cur_max + dp(i+1, jobDifficulty[i+1], remain-1)
            return min(include, not_include)

        result = dp(0, jobDifficulty[0], d)
        return -1 if result == float('inf') else result


start_time = time()

_jobDifficulty = [6,5,4,3,2,1]
_d = 2
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7

print(Solution().minDifficulty(_jobDifficulty, _d))

print("--- %s seconds ---" % (time() - start_time))
