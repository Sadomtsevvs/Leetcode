from collections import defaultdict
from functools import cache
from time import time
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        idxs = {}
        for i in range(len(words[0])):
            idx = defaultdict(int)
            for word in words:
                idx[word[i]] += 1
            idxs[i] = idx

        @cache
        def helper(idx_tg, idx_cur):
            if idx_tg == len(target):
                return 1
            if idx_cur == len(words[0]):
                return 0
            if len(words[0]) - idx_cur < len(target) - idx_tg:
                return 0
            char = target[idx_tg]
            result = helper(idx_tg, idx_cur + 1)  # this idea I saw from LC comments, skip the current index
            if char in idxs[idx_cur]:
                result += helper(idx_tg + 1, idx_cur + 1) * idxs[idx_cur][char]
            return result % (10 ** 9 + 7)

        return helper(0, 0)

        # my first solution, good, but TLE
        #
        # idxs = {}
        # for i in range(len(words[0])):
        #     idx = defaultdict(int)
        #     for word in words:
        #         idx[word[i]] += 1
        #     idxs[i] = idx
        #
        # @cache
        # def helper(idx_tg, idx_cur):
        #     if idx_tg == len(target):
        #         return 1
        #     if idx_cur == len(words[0]):
        #         return 0
        #     if len(words[0]) - idx_cur < len(target) - idx_tg:
        #         return 0
        #     char = target[idx_tg]
        #     result = 0
        #     for i in range(idx_cur, len(words[0])):
        #         if char in idxs[i]:
        #             result += helper(idx_tg+1, i+1) * idxs[i][char]
        #     return result % (10**9 + 7)
        #
        # return helper(0, 0)


start_time = time()

# Example 1:
# Input: words = ["acca","bbbb","caca"], target = "aba"
_words = ["acca", "bbbb", "caca"]
_target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
#
# Example 2:
# Input: words = ["abba","baab"], target = "bab"
_words = ["abba", "baab"]
_target = "bab"
# Output: 4
# Explanation: There are 4 ways to form target.
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
# "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
# "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

_words = ["cabbaacaaaccaabbbbaccacbabbbcb", "bbcabcbcccbcacbbbaacacaaabbbac", "cbabcaacbcaaabbcbaabaababbacbc",
          "aacabbbcaaccaabbaccacabccaacca", "bbabbaabcaabccbbabccaaccbabcab", "bcaccbbaaccaabcbabbacaccbbcbbb",
          "cbbcbcaaaacacabbbabacbaabbabaa", "cbbbbbbcccbabbacacacacccbbccca", "bcbccbccacccacaababcbcbbacbbbc",
          "ccacaabaaabbbacacbacbaaacbcaca", "bacaaaabaabccbcbbaacacccabbbcb", "bcbcbcabbccabacbcbcaccacbcaaab",
          "babbbcccbbbbbaabbbacbbaabaabcc", "baaaacaaacbbaacccababbaacccbcb", "babbaaabaaccaabacbbbacbcbababa",
          "cbacacbacaaacbaaaabacbbccccaca", "bcbcaccaabacaacaaaccaabbcacaaa", "cccbabccaabbcbccbbabaaacbacaaa",
          "bbbcabacbbcabcbcaaccbcacacccca", "ccccbbaababacbabcaacabaccbabaa", "caaabccbcaaccabbcbcaacccbcacba",
          "cccbcaacbabaacbaaabbbbcbbbbcbb", "cababbcacbabcbaababcbcabbaabba", "aaaacacaaccbacacbbbbccaabcccca",
          "cbcaaaaabacbacaccbcbcbccaabaac", "bcbbccbabaccabcccacbbaacbbcbba", "cccbabbbcbbabccbbabbbbcaaccaab",
          "acccacccaabbcaccbcaaccbababacc", "bcacabaacccbbcbbacabbbbbcaaaab", "cacccaacbcbccbabccabbcbabbcacc",
          "aacabbabcaacbaaacaabcabcaccaab", "cccacabacbabccbccaaaaabbcacbcc", "cabaacacacaaabaacaabababccbaaa",
          "caabaccaacccbaabcacbcbbabccabc", "bcbbccbbaaacbaacbccbcbababcacb", "bbabbcabcbbcababbbbccabaaccbca",
          "cacbbbccabaaaaccacbcbabaabbcba", "ccbcacbabababbbcbcabbcccaccbca", "acccabcacbcbbcbccaccaacbabcaab",
          "ccacaabcbbaabaaccbabcbacaaabaa", "cbabbbbcabbbbcbccabaabccaccaca", "acbbbbbccabacabcbbabcaacbbaacc",
          "baaababbcabcacbbcbabacbcbaaabc", "cabbcabcbbacaaaaacbcbbcacaccac"]
_target = "acbaccacbbaaabbbabac"

print(Solution().numWays(_words, _target))

print("--- %s seconds ---" % (time() - start_time))
