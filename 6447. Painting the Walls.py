from functools import cache
from time import time
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        ans = [float('inf')]

        @cache
        def dfs(cur_ind, cur_sum, time_paid, to_paint):
            if time_paid >= to_paint:
                ans[0] = min(ans[0], cur_sum)
                return
            if cur_ind == len(cost):
                return
            for i in range(cur_ind, len(cost)):
                dfs(i + 1, cur_sum + cost[i], time_paid + time[i], to_paint - 1)
            dfs(cur_ind+1, cur_sum, time_paid, to_paint)

        dfs(0, 0, 0, len(cost))

        return ans[0]


start_time = time()

# Example 1:
# Input: cost = [1,2,3,2], time = [1,2,3,2]
_cost = [1,2,3,2]
_time = [1,2,3,2]
# Output: 3
# Explanation: The walls at index 0 and 1 will be painted by the paid painter, and it will take 3 units of time; meanwhile, the free painter will paint the walls at index 2 and 3, free of cost in 2 units of time. Thus, the total cost is 1 + 2 = 3.
#
# Example 2:
# Input: cost = [2,3,4,2], time = [1,1,1,1]
_cost = [2,3,4,2]
_time = [1,1,1,1]
# Output: 4
# Explanation: The walls at index 0 and 3 will be painted by the paid painter, and it will take 2 units of time; meanwhile, the free painter will paint the walls at index 1 and 2, free of cost in 2 units of time. Thus, the total cost is 2 + 2 = 4.

_cost = [937,252,716,781,319,198,273,554,140,68,694,583,1080,16,450,229,710,1003,1117,1036,398,874,289,664,600,588,372,1066,375,532,984,328,1067,746]
_time = [5,3,1,3,2,1,3,3,5,3,5,5,4,1,3,1,4,4,4,1,5,1,2,3,2,3,3,4,1,3,4,1,1,5]

print(Solution().paintWalls(_cost, _time))

print("--- %s seconds ---" % (time() - start_time))
