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

        # my second solution, working, but no efficient
        #
        # @cache
        # def dp(to_get, i):
        #     if to_get == 0:
        #         return 1
        #     if to_get < 0:
        #         return 0
        #     if i == len(coins):
        #         return 0
        #     coin = coins[i]
        #     result = 0
        #     for j in range(to_get // coin + 1):
        #         result += dp(to_get - coin * j, i + 1)
        #     return result
        #
        # return dp(amount, 0)


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
