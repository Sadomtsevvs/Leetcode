from collections import defaultdict
from time import time
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = defaultdict(list)
        for i, boss in enumerate(manager):
            subs[boss].append(i)
        ans = 0
        bosses = [(headID, informTime[headID])]
        while bosses:
            boss, t = bosses.pop()
            ans = max(ans, t)
            for sub in subs[boss]:
                bosses.append((sub, t + informTime[sub]))
        return ans


start_time = time()

# Example 1:
# Input: n = 1, headID = 0, manager = [-1], informTime = [0]
# Output: 0
# Explanation: The head of the company is the only employee in the company.
#
# Example 2:
# Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
_n = 6
_headID = 2
_manager = [2,2,-1,2,2,2]
_informTime = [0,0,1,0,0,0]
# Output: 1
# Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
# The tree structure of the employees in the company is shown.

print(Solution().numOfMinutes(_n, _headID, _manager, _informTime))

print("--- %s seconds ---" % (time() - start_time))
