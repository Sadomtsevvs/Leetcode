from functools import cache
from time import time
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dictionary = set(dictionary)

        @cache
        def dfs(i):
            if i >= len(s):
                return 0
            result = len(s) - i
            cands = []
            for j in range(i, len(s)):
                char = s[j]
                cands = [cand + char for cand in cands]
                cands.append(char)
                for cand in cands:
                    if cand in dictionary:
                        ans = j - i + 1 - len(cand) + dfs(j + 1)
                        result = min(result, ans)
            return result

        return dfs(0)


start_time = time()

# Example 1:
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.
#
# Example 2:
# Input: s = "sayhelloworld", dictionary = ["hello","world"]
_s = "sayhelloworld"
_dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

# Input:
_s = "dwmodizxvvbosxxw"
_dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
# Output: 9
# Expected: 7

print(Solution().minExtraChar(_s, _dictionary))

print("--- %s seconds ---" % (time() - start_time))
