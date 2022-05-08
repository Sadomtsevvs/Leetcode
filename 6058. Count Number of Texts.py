from time import time


class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        digits = [0, 0, 2, 2, 2, 2, 2, 3, 2, 3]

        dp = [0] * (len(pressedKeys) + 1)
        dp[0] = 1
        mod = 10**9 + 7

        for i in range(1, len(pressedKeys) + 1):
            char = pressedKeys[i-1]
            dp[i] += dp[i-1]
            for j in range(digits[int(char)]):
                if i-j-2 < 0:
                    break
                if pressedKeys[i-j-2] == char:
                    dp[i] += dp[i-j-2]
                else:
                    break
            dp[i] %= mod
        return dp[-1]


start_time = time()

_pressedKeys = "22222"
# _pressedKeys = "222222222222222222222222222222222222"
# _pressedKeys = "243244345465654626473534254657657878867855555555555555555555554676875559984764"
# Input: pressedKeys = "22233"
# Output: 8
# Explanation:
# The possible text messages Alice could have sent are:
# "aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
# Since there are 8 possible messages, we return 8.

print(Solution().countTexts(_pressedKeys))

print("--- %s seconds ---" % (time() - start_time))
