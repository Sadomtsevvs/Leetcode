from time import time
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP bottom up solution
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return max(dp[n-1][0], dp[n-1][1])

        # approach from LC: buy low, sell high
        # n = len(prices)
        # ans = 0
        # for i in range(1, n):
        #     if prices[i] > prices[i-1]:
        #         ans += prices[i] - prices[i-1]
        # return ans

        # return sum(P[i] - P[i - 1] if P[i] > P[i - 1] else 0 for i in range(1, len(P)))


start_time = time()

_prices = [7,1,5,3,6,4]
# _prices = [1,2,3,4,5]
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

print(Solution().maxProfit(_prices))

print("--- %s seconds ---" % (time() - start_time))
