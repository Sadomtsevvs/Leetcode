from time import time


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        res = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if len(word) > i:
                    continue
                if res[i-len(word)] and s[i-len(word):i] == word:
                    res[i] = True
                    break
        return res[len(s)]


start_time = time()

_s = "catsandog"
_wordDict = ["cats","dog","sand","and","cat"]
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

print(Solution().wordBreak(_s, _wordDict))

print("--- %s seconds ---" % (time() - start_time))
