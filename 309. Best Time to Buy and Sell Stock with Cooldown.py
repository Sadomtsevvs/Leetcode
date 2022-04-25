from time import time
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # top-down solution

        # @lru_cache(None)
        # def dp(day, holding, cooldown):
        #     # Base case
        #     if day == len(prices):
        #         return 0
        #
        #     do_nothing = dp(day + 1, holding, 0)
        #
        #     if holding:
        #         # Sell stock
        #         do_something = prices[day] + dp(day + 1, 0, 1)
        #     elif not cooldown:
        #         # Buy stock
        #         do_something = -prices[day] + dp(day + 1, 1, 0)
        #     else:
        #         do_something = 0
        #
        #     # Recurrence relation
        #     return max(do_nothing, do_something)
        #
        # return dp(0, 0, 0)

        # bottom-up solution

        dp = [[[0] * 2 for _ in range(2)] for __ in range(len(prices) + 1)]
        for day in range(len(prices) - 1, -1, -1):
            for having in range(2):
                for cooldown in range(2):
                    do_nothing = dp[day+1][having][0]
                    if having:
                        do_something = prices[day] + dp[day+1][0][1]
                    elif not cooldown:
                        do_something = -prices[day] + dp[day + 1][1][0]
                    else:
                        do_something = 0
                    dp[day][having][cooldown] = max(do_nothing, do_something)
        return dp[0][0][0]


start_time = time()

_prices = [1,2,3,0,2]
# Input: prices = [1,2,3,0,2]
# Output: 3

print(Solution().maxProfit(_prices))

print("--- %s seconds ---" % (time() - start_time))
