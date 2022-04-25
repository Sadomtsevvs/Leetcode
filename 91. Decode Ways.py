from time import time


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        if int(s[:2]) <= 26:
            if s[1] == '0':
                singles, pairs = 0, 1
            else:
                singles, pairs = 1, 1
        elif s[1] == '0':
            return 0
        else:
            singles, pairs = 1, 0
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i-1] == '0' or int(s[i-1]) >= 3:
                    return 0
                else:
                    singles, pairs = 0, singles
            elif int(s[i-1:i+1]) > 26:
                singles, pairs = singles + pairs, 0
            elif s[i-1] == '0':
                singles, pairs = pairs, 0
            elif int(s[i-1:i+1]) <= 26:
                if int(s[i-2:i]) > 26:
                    pairs = singles
                else:
                    singles, pairs = singles + pairs, singles
        return singles + pairs

        # fastest solution from LC comments
        #
        # dp = [0 for i in range(len(s) + 1)]
        # dp[0] = 1
        # dp[1] = 0 if s[0] == '0' else 1
        # for i in range(2, len(dp)):
        #     if s[i - 1] != '0':
        #         dp[i] = dp[i - 1]
        #     if 10 <= int(s[i - 2:i]) <= 26:
        #         dp[i] += dp[i - 2]
        # return dp[len(s)]

start_time = time()

_s = "111111"
# _s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

print(Solution().numDecodings(_s))

print("--- %s seconds ---" % (time() - start_time))
