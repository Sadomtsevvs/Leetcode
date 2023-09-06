from time import time


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalties_n = [0] * (n + 1)
        penalties_y = [0] * (n + 1)
        for i in range(n):
            day_n, day_y = customers[i], customers[n-i-1]
            penalties_n[i+1] = penalties_n[i] + (1 if day_n == 'N' else 0)
            penalties_y[n-i-1] = penalties_y[n-i] + (1 if day_y == 'Y' else 0)
        penalty = n + 1
        ans = 0
        for time in range(n+1):
            cur_penalty = penalties_n[time] + penalties_y[time]
            if cur_penalty < penalty:
                penalty = cur_penalty
                ans = time
        return ans

        # official solution
        #
        # # Start with closing at hour 0, the penalty equals all 'Y' in closed hours.
        # cur_penalty = min_penalty = customers.count('Y')
        # earliest_hour = 0
        #
        # for i, ch in enumerate(customers):
        #     # If status in hour i is 'Y', moving it to open hours decrement
        #     # penalty by 1. Otherwise, moving 'N' to open hours increment
        #     # penatly by 1.
        #     if ch == 'Y':
        #         cur_penalty -= 1
        #     else:
        #         cur_penalty += 1
        #
        #     # Update earliest_hour if a smaller penatly is encountered
        #     if cur_penalty < min_penalty:
        #         earliest_hour = i + 1
        #         min_penalty = cur_penalty
        #
        # return earliest_hour


start_time = time()

# Example 1:
# Input: customers = "YYNY
_customers = "YYNY"
# Output: 2
# Explanation:
# - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
#
# Example 2:
# Input: customers = "NNNNN"
# _customers = "NNNNN"
# Output: 0
# Explanation: It is best to close the shop at the 0th hour as no customers arrive.
#
# Example 3:
# Input: customers = "YYYY"
# _customers = "YYYY"
# Output: 4
# Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

print(Solution().bestClosingTime(_customers))

print("--- %s seconds ---" % (time() - start_time))
