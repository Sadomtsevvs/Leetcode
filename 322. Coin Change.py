from time import time


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        res = [0]
        for i in range(1, amount + 1):
            best = [res[i - k] for k in coins if i - k >= 0 and res[i - k] >= 0]
            if not best:
                res.append(-1)
            else:
                res.append(1 + min(best))
        return res[amount]


start_time = time()

_coins = [3, 7]
_amount = 16
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

print(Solution().coinChange(_coins, _amount))

print("--- %s seconds ---" % (time() - start_time))
