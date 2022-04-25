from time import time


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        # solution with O(n) space complexity
        #
        # result = [0] * (len(cost) + 1)
        # for i in range(2, len(cost) + 1):
        #     result[i] = min(result[i-2] + cost[i-2], result[i-1] + cost[i-1])
        # return result[-1]

        # solution with O(1) space complexity

        prev, before_prev = 0, 0
        for i in range(2, len(cost) + 1):
            prev, before_prev = min(before_prev + cost[i-2], prev + cost[i-1]), prev
        return prev

start_time = time()

_cost = [1,100,1,1,1,100,1,1,100,1]
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

print(Solution().minCostClimbingStairs(_cost))

print("--- %s seconds ---" % (time() - start_time))
