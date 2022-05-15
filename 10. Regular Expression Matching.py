from time import time


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # if not p:
        #     return not s
        #
        # first_match = len(s) > 0 and p[0] in {s[0], '.'}
        #
        # if len(p) > 1 and p[1] == '*':
        #     return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])


        # re = []
        # for char in p:
        #     if char == '*':
        #         re[-1] += '*'
        #     else:
        #         re.append(char)
        #
        # def dp(i, j):
        #     if i < 0 and j < 0:
        #         return True
        #     if j < 0 or i < 0:
        #         return False
        #     dp_i1_j = dp(i - 1, j)
        #     dp_i1_j1 = dp(i - 1, j - 1)
        #     return (i > 0 and dp_i1_j and (s[i] == s[i - 1] and (re[j] == s[i]+"*" or re[j] == '.*'))) \
        #            or (dp_i1_j1 and (s[i] == re[j] or re[j] == '.' or re[j] == s[i]+"*"))
        #     # return (dp(i - 1, j) and (s[i] == s[i - 1] and (re[j] == s[i]+"*" or re[j] == '.*'))) \
        #     #        or (dp(i - 1, j - 1) and (s[i] == re[j] or re[j] == '.'))
        #
        # return dp(len(s) - 1, len(re) - 1)

        # official solution
        #
        # if not pattern:
        #     return not text
        #
        # first_match = bool(text) and pattern[0] in {text[0], '.'}
        #
        # if len(pattern) >= 2 and pattern[1] == '*':
        #     return (self.isMatch(text, pattern[2:]) or
        #             first_match and self.isMatch(text[1:], pattern))
        # else:
        #     return first_match and self.isMatch(text[1:], pattern[1:])

        # solution from LC
        #
        # prev = [False, True]
        # for j in range(len(p)):
        #     prev.append(p[j] == '*' and prev[j])
        #
        # for i in range(len(s)):
        #     curr = [False, False]
        #     for j in range(len(p)):
        #         if p[j] == '*':
        #             curr.append(curr[j] or curr[j + 1] or (prev[j + 2] and p[j - 1] in (s[i], '.')))
        #         else:
        #             curr.append(prev[j + 1] and p[j] in (s[i], '.'))
        #     prev = curr
        # return prev[-1]

        # solution from LC
        #
        s, p = ' '+ s, ' '+ p
        lenS, lenP = len(s), len(p)
        dp = [[0]*(lenP) for i in range(lenS)]
        dp[0][0] = 1

        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

        return bool(dp[-1][-1])


start_time = time()

_s = "aaaaaaa"
_p = ".*"
_s = "aa"
_p = "a*b*"
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

print(Solution().isMatch(_s, _p))

print("--- %s seconds ---" % (time() - start_time))
