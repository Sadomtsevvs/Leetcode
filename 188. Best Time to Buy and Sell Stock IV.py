from time import time
from functools import lru_cache


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        @lru_cache(None)
        def dp(i, transactions_remaining, holding):
            # Base case
            if transactions_remaining == 0 or i == len(prices):
                return 0

            do_nothing = dp(i + 1, transactions_remaining, holding)

            if holding:
                # Sell stock
                do_something = prices[i] + dp(i + 1, transactions_remaining - 1, 0)
            else:
                # Buy stock
                do_something = -prices[i] + dp(i + 1, transactions_remaining, 1)

            # Recurrence relation
            return max(do_nothing, do_something)

        return dp(0, k, 0)


start_time = time()

_k = 2
_prices = [3,2,6,5,0,3]
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5
# (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

print(Solution().maxProfit(_k, _prices))

print("--- %s seconds ---" % (time() - start_time))