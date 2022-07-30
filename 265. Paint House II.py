from time import time
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        # time O(n*k)
        # space O(k)

        def best_results(result):
            first_best = float('inf')
            idx_best = -1
            second_best = float('inf')
            for j in range(len(costs[0])):
                price = result[j]
                if price < first_best:
                    second_best = first_best
                    first_best = price
                    idx_best = j
                elif price < second_best:
                    second_best = price
            return first_best, second_best, idx_best

        dp = costs[0]
        first_best, second_best, idx_best = best_results(dp)
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                if j == idx_best:
                    dp[j] = costs[i][j] + second_best
                else:
                    dp[j] = costs[i][j] + first_best
            first_best, second_best, idx_best = best_results(dp)
        return min(dp)

        # first solution
        # time O(n*k*k)
        # space O(n*k)
        #
        # dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))]
        # dp[0] = costs[0]
        # for i in range(1, len(costs)):
        #     for j in range(len(costs[0])):
        #         prev_best = float('inf')
        #         for k in range(len(costs[0])):
        #             if k == j:
        #                 continue
        #             prev_best = min(prev_best, dp[i-1][k])
        #         dp[i][j] = costs[i][j] + prev_best
        # return min(dp[-1])


start_time = time()

_costs = [[1,5,3],[2,9,4]]
# Example 1:
# Input: costs = [[1,5,3],[2,9,4]]
# Output: 5
# Explanation:
# Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
#
# Example 2:
# Input: costs = [[1,3],[2,4]]
# Output: 5

print(Solution().minCostII(_costs))

print("--- %s seconds ---" % (time() - start_time))
