from time import time
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict = set(wordDict)

        result = []

        def get_words(remain, cur):
            if remain == '':
                result.append(" ".join(cur))
                return
            for i in range(len(remain)):
                word = remain[:i + 1]
                if word in wordDict:
                    get_words(remain[i + 1:], cur + [word])

        get_words(s, [])

        return result


start_time = time()

_s = "catsanddog"
_wordDict = ["cat","cats","and","sand","dog"]
# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#
# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

print(Solution().wordBreak(_s, _wordDict))

print("--- %s seconds ---" % (time() - start_time))
