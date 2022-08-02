from collections import Counter, defaultdict
from time import time
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        # second solution: create one Counter from all words2
        # O(w1 * ww1 + w2 * ww2 + ww2 * w1
        words1 = {word: Counter(word) for word in words1}
        dic2 = defaultdict(int)
        for word2 in words2:
            word2 = Counter(word2)
            for char, count in word2.items():
                dic2[char] = max(dic2[char], count)
        for char, count in dic2.items():
            next_round = {}
            for word1, cntr1 in words1.items():
                if cntr1[char] >= count:
                    next_round[word1] = cntr1
            words1 = next_round
        return list(words1.keys())

        # first solution, TLE, O(w1 * ww1 + w2 * ww2 * w1)
        # words1 = {word: Counter(word) for word in words1}
        # for word2 in words2:
        #     word2 = Counter(word2)
        #     for char, count in word2.items():
        #         next_round = {}
        #         for word1, cntr1 in words1.items():
        #             if cntr1[char] >= count:
        #                 next_round[word1] = cntr1
        #         words1 = next_round
        # return list(words1.keys())

        # official solution
        #
        # def count(word):
        #     ans = [0] * 26
        #     for letter in word:
        #         ans[ord(letter) - ord('a')] += 1
        #     return ans
        #
        # bmax = [0] * 26
        # for b in B:
        #     for i, c in enumerate(count(b)):
        #         bmax[i] = max(bmax[i], c)
        #
        # ans = []
        # for a in A:
        #     if all(x >= y for x, y in zip(count(a), bmax)):
        #         ans.append(a)
        # return ans

        # from Lee
        #
        # count = collections.Counter()
        # for b in B:
        #     count |= collections.Counter(b)
        # return [a for a in A if not count - Counter(a)]


start_time = time()

_words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
_words2 = ["e", "o"]
# Example 1:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]
#
_words1 = ["amazon","apple","facebook","google","leetcode"]
_words2 = ["l","e"]
# Example 2:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
# Output: ["apple","google","leetcode"]

print(Solution().wordSubsets(_words1, _words2))

print("--- %s seconds ---" % (time() - start_time))
