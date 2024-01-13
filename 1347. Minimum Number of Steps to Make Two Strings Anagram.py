from collections import Counter
from time import time


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)
        result = 0
        for value in (cs - ct).values():
            result += value
        return result


start_time = time()

# Example 1:
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
#
# Example 2:
# Input: s = "leetcode", t = "practice"
_s = "leetcode"
_t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
#
# Example 3:
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams.

print(Solution().minSteps(_s, _t))

print("--- %s seconds ---" % (time() - start_time))
