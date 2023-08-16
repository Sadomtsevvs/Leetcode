from bisect import bisect_left
from collections import defaultdict
from functools import cache
from time import time


class Solution:
    def strangePrinter(self, s: str) -> int:

        ends = defaultdict(set)
        for i, char in enumerate(s):
            if i - 1 in ends[char]:
                ends[char].remove(i-1)
            ends[char].add(i)

        ends_list = defaultdict(list)
        for char, sets in ends.items():
            ends_list[char] = sorted(list(ends[char]))

        @cache
        def dfs(i, cur):
            if i == len(s):
                return 0
            char = s[i]
            if not cur:
                return 1 + dfs(i + 1, char * len(s))
            if cur and cur[i] == char:
                return dfs(i + 1, cur)
            result = 101
            start = bisect_left(ends_list[char], i)
            for ind in range(start, len(ends_list[char])):
                j = ends_list[char][ind]
            # for j in ends[char]:
                if j < i:
                    continue
                result = min(result, 1 + dfs(i + 1, cur[:i] + char * (j - i + 1) + cur[j + 1:]))
            # for j in range(i, len(s)):
            #     result = min(result, 1 + dfs(i + 1, cur[:i] + char * (j - i + 1) + cur[j + 1:]))
            return result

        return dfs(0, '')


start_time = time()

# Example 1:
# Input: s = "aaabbb"
_s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
#
# Example 2:
# Input: s = "aba"
# _s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

_s = "aaaababa"
_s = "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"
_s = "adaabdacccccaaabbdbadbcdcdcdddcabbdacbcbaababddcaa"

print(Solution().strangePrinter(_s))

print("--- %s seconds ---" % (time() - start_time))
