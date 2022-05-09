from time import time


class Solution:
    def canGetExactChange(self, targetMoney, denominations):
        dp = [True]
        for i in range(1, targetMoney + 1):
            result = False
            for coin in denominations:
                if i - coin < 0:
                    continue
                result = result or dp[i-coin]
            dp.append(result)
        return dp[-1]


start_time = time()

_denominations = [5, 10, 25, 100, 200]
_targetMoney = 94
_denominations = [4, 17, 29]
_targetMoney = 75
# denominations = [5, 10, 25, 100, 200]
# targetMoney = 94
# output = false

print(Solution().canGetExactChange(_targetMoney, _denominations))

print("--- %s seconds ---" % (time() - start_time))
