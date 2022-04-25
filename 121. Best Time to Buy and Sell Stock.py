from time import time


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # top-down solution, slow
        #
        # def dp(day, having, deals):
        #     if day == len(prices) or deals == 1:
        #         return 0
        #     do_nothing = dp(day + 1, having, deals)
        #     if having:
        #         do_something = prices[day] + dp(day + 1, 0, deals + 1)
        #     else:
        #         do_something = - prices[day] + dp(day + 1, 1, deals)
        #     return max(do_nothing, do_something)
        #
        # return dp(0, 0, 0)

        # bottom-up solution, better speed
        #
        # dp = [[[0] * 2 for _ in range(2)] for __ in range(len(prices) + 1)]
        # for day in range(len(prices) - 1, -1, -1):
        #     for having in range(2):
        #         do_nothing = dp[day+1][having][0]
        #         if having:
        #             do_somethind = prices[day] + dp[day+1][0][1]
        #         else:
        #             do_somethind = -prices[day] + dp[day+1][1][0]
        #         dp[day][having][0] = max(do_nothing, do_somethind)
        # return dp[0][0][0]

        # Kadane's algorithm
        if len(prices) < 2:
            return 0
        buy, best = prices[0], 0
        for day in prices:
            buy = min(buy, day)
            best = max(best, day - buy)
        return best



start_time = time()

_prices = [7,1,5,3,6,4]
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

print(Solution().maxProfit(_prices))

print("--- %s seconds ---" % (time() - start_time))
