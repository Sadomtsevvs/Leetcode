from time import time


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 1
        ans += total // cost1
        ans += total // cost2
        while cost1 <= total:
            total -= cost1
            ans += total // cost2
        return ans


start_time = time()

_total = 20
_cost1 = 10
_cost2 = 5
_total = 5
_cost1 = 10
_cost2 = 10
# Input: total = 20, cost1 = 10, cost2 = 5
# Output: 9
# Explanation: The price of a pen is 10 and the price of a pencil is 5.
# - If you buy 0 pens, you can buy 0, 1, 2, 3, or 4 pencils.
# - If you buy 1 pen, you can buy 0, 1, or 2 pencils.
# - If you buy 2 pens, you cannot buy any pencils.
# The total number of ways to buy pens and pencils is 5 + 3 + 1 = 9.

print(Solution().waysToBuyPensPencils(_total, _cost1, _cost2))

print("--- %s seconds ---" % (time() - start_time))
