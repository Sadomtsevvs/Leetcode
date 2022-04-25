from time import time


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1



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
