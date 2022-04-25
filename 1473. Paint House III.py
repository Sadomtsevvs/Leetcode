from time import time
from functools import lru_cache


class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, j, k):

            if i == m:
                if k == 0:
                    return 0
                return float('inf')
            if k == 0:
                return float('inf')

            mincost = float('inf')

            if houses[i] != 0:
                if j != houses[i]:
                    return float('inf')
                for next_color in range(1, n+1):
                    if j == next_color:
                        mincost = min(mincost, dp(i+1, j, k))
                    else:
                        mincost = min(mincost, dp(i+1, next_color, k-1))
            else:
                for next_color in range(1, n+1):
                    if j == next_color:
                        mincost = min(mincost, cost[i][j-1] + dp(i+1, j, k))
                    else:
                        mincost = min(mincost, cost[i][j-1] + dp(i+1, next_color, k-1))
            return mincost

        result = min([dp(0, color, target) for color in range(1, n+1)])
        return result if result != float('inf') else -1


start_time = time()

# _houses = [0,0,0,1]
# _cost = [[1,5],[4,1],[1,3],[4,4]]
# _m = 4
# _n = 2
# _target = 4
# _houses = [3,1,2,3]
# _cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
# _m = 4
# _n = 3
# _target = 3
# _houses = [0,2,1,2,0]
# _cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
# _m = 5
# _n = 2
# _target = 3
_houses = [0,0,0,0,0]
_cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
_m = 5
_n = 2
_target = 3
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

print(Solution().minCost(_houses, _cost, _m, _n, _target))

print("--- %s seconds ---" % (time() - start_time))
