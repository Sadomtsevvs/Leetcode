from time import time


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        res = [0] * (amount + 1)
        res[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin < 0:
                    continue
                res[i] += res[i-coin]
        return res[amount]


start_time = time()

_amount = 10
_coins = [1, 2, 5]
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

print(Solution().change(_amount, _coins))

print("--- %s seconds ---" % (time() - start_time))
