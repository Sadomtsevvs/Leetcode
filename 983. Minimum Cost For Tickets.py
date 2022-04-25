from time import time


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        days_hash = dict.fromkeys(days)
        dp = [0] * (max(days) + 1)
        for day in range(1, max(days) + 1):
            if day in days_hash:
                if day < 7:
                    dp[day] = min(dp[day-1] + costs[0], 0 + costs[1], 0 + costs[2])
                elif day < 30:
                    dp[day] = min(dp[day-1] + costs[0], dp[day-7] + costs[1], 0 + costs[2])
                else:
                    dp[day] = min(dp[day-1] + costs[0], dp[day-7] + costs[1], dp[day-30] + costs[2])
            else:
                dp[day] = dp[day-1]
        return dp[-1]


start_time = time()

_days = [1,2,3,4,5,6,7,8,9,10,30,31]
_costs = [2,7,15]
# _days = [1,4,6,7,8,20]
# _costs = [2,7,15]
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.

print(Solution().mincostTickets(_days, _costs))

print("--- %s seconds ---" % (time() - start_time))
