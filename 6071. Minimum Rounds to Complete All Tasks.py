from time import time
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        ans = 0
        for c in Counter(tasks).values():
            if c == 1:
                return -1
            a, b = divmod(c, 3)
            ans += a
            if b != 0:
                ans += 1
        return ans


start_time = time()

_tasks = [2,2,3,3,2,4,4,4,4,4]
_tasks = [2,3,3]
# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2.
# - In the second round, you complete 2 tasks of difficulty level 3.
# - In the third round, you complete 3 tasks of difficulty level 4.
# - In the fourth round, you complete 2 tasks of difficulty level 4.
# It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

print(Solution().minimumRounds(_tasks))

print("--- %s seconds ---" % (time() - start_time))
