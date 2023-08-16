import heapq
from time import time
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cst = [(costs[i], 0 if i < candidates else 1) for i in range(len(costs)) if i < candidates or i > len(costs) - candidates - 1]
        heapq.heapify(cst)
        left = candidates - 1
        right = len(costs) - candidates
        ans = 0
        workers = 0
        while workers < k:
            cost, side = heapq.heappop(cst)
            ans += cost
            workers += 1
            if left + 1 < right:
                if side == 0:
                    left += 1
                    heapq.heappush(cst, (costs[left], side))
                else:
                    right -= 1
                    heapq.heappush(cst, (costs[right], side))
        return ans


start_time = time()

# Example 1:
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.
#
# Example 2:
# Input: costs = [1,2,4,1], k = 3, candidates = 3
_costs = [1,2,4,1]
_k = 3
_candidates = 3
# Output: 4
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
# - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
# - In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
# The total hiring cost is 4.

# Input
# [28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34]
# 32
# 12
_costs = [28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34]
_k = 32
_candidates = 12
# Output
# 1404
# Expected
# 1407

print(Solution().totalCost(_costs, _k, _candidates))

print("--- %s seconds ---" % (time() - start_time))
