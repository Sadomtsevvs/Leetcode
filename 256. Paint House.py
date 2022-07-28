from time import time
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        # O(1) space solution
        #
        prev_0, prev_1, prev_2 = costs[0]
        for i in range(1, len(costs)):
            prev_0, prev_1, prev_2 = costs[i][0] + min(prev_1, prev_2),\
                                     costs[i][1] + min(prev_0, prev_2),\
                                     costs[i][2] + min(prev_0, prev_1)
        return min(prev_0, prev_1, prev_2)

        # my first solution
        #
        # dp = [[0, 0, 0] for _ in range(len(costs))]
        # dp[0] = costs[0]
        # for i in range(1, len(costs)):
        #     dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        #     dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        #     dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        # return min(dp[-1])


start_time = time()

_costs = [[17,2,17],[16,16,5],[14,3,19]]
# Example 1:
# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.
#
# Example 2:
# Input: costs = [[7,6,2]]
# Output: 2

print(Solution().minCost(_costs))

print("--- %s seconds ---" % (time() - start_time))
