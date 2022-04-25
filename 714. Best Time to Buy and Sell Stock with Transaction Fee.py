from time import time
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:

        # top-down solution
        #
        # def dp(day, holding):
        #
        #     if day == len(prices):
        #         return 0
        #
        #     do_nothing = dp(day + 1, holding)
        #
        #     if holding:
        #         # Sell stock
        #         do_something = prices[day] - fee + dp(day + 1, 0)
        #     else:
        #         # Buy stock
        #         do_something = -prices[day] + dp(day + 1, 1)
        #
        #     # Recurrence relation
        #     return max(do_nothing, do_something)
        #
        # return dp(0, 0)

        # bottom-up solution

        dp = [[0]*2 for _ in range(len(prices)+1)]

        for day in range(len(prices)-1, -1, -1):
            for holding in range(2):

                do_nothing = dp[day + 1][holding]

                if holding:
                    # Sell stock
                    do_something = prices[day] - fee + dp[day + 1][0]
                else:
                    # Buy stock
                    do_something = -prices[day] + dp[day + 1][1]

                # Recurrence relation
                dp[day][holding] = max(do_nothing, do_something)

        return dp[0][0]

        # official solution
        #
        # cash, hold = 0, -prices[0]
        # for i in range(1, len(prices)):
        #     cash = max(cash, hold + prices[i] - fee)
        #     hold = max(hold, cash - prices[i])
        # return cash


start_time = time()

_prices = [2,1,3,8,4,9]
_fee = 2
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

print(Solution().maxProfit(_prices, _fee))

print("--- %s seconds ---" % (time() - start_time))
