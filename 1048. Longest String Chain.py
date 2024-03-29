from collections import defaultdict
from time import time
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        # my forth solution
        def is_predecessor(word1, word2):
            i, j = 0, 0
            skip = False
            for j in range(len(word2)):
                if i == len(word1):
                    return True
                if word1[i] == word2[j]:
                    i += 1
                elif not skip:
                    skip = True
                else:
                    return False
            return True

        d = defaultdict(list)
        chains = dict()
        for word in words:
            d[len(word)].append(word)
            chains[word] = 1

        for word1 in sorted(words, key=len):
            for word2 in d[len(word1) + 1]:
                if is_predecessor(word1, word2):
                    chains[word2] = max(chains[word2], chains[word1] + 1)

        return max(chains.values())

        # # my third solution
        # def is_predecessor(pred_word, word):
        #     was_mistake = False
        #     w = 0
        #     p = 0
        #     while w < len(word) and p < len(pred_word):
        #         if word[w] != pred_word[p]:
        #             if was_mistake:
        #                 return False
        #             else:
        #                 was_mistake = True
        #                 w += 1
        #         else:
        #             w += 1
        #             p += 1
        #     return True
        #
        # lsc = dict()
        # d_w = defaultdict(list)
        # for word in set(words):
        #     lsc[word] = 1
        #     d_w[len(word)].append(word)
        # for l in sorted(d_w.keys()):
        #     for word in d_w[l]:
        #         result = 0
        #         for pred_word in d_w[l - 1]:
        #             if is_predecessor(pred_word, word):
        #                 result = max(result, lsc[pred_word])
        #         lsc[word] += result
        # return max(lsc.values())


    # def is_predecessor(self, pred, string):
    #     pp, ss = 0, 0
    #     added = False
    #     while pp < len(pred):
    #         if pred[pp] == string[ss]:
    #             pp += 1
    #             ss += 1
    #         elif not added:
    #             ss += 1
    #             added = True
    #         else:
    #             return False
    #     return True
    #
    # def longestStrChain(self, words: List[str]) -> int:
    #     # a bit different solution
    #     words = [(word, len(word)) for word in words]
    #     words.sort(key=lambda x: x[1])
    #     dp = [1] * len(words)
    #     for i in range(1, len(words)):
    #         result = 1
    #         wi = words[i][0]
    #         len_wi = words[i][1]
    #         for j in range(i-1, -1, -1):
    #             wj = words[j][0]
    #             len_wj = words[j][1]
    #             if len_wj == len_wi:
    #                 continue
    #             elif len_wj + 1 < len_wi:
    #                 break
    #             elif self.is_predecessor(wj, wi):
    #                 result = max(result, dp[j] + 1)
    #         dp[i] = result
    #     return max(dp)

        # first solution
        #
        # words.sort(key=len)
        # dp = [1] * len(words)
        # for i in range(1, len(words)):
        #     result = 1
        #     for j in range(i-1, -1, -1):
        #         if len(words[j]) == len(words[i]):
        #             continue
        #         elif len(words[j]) + 1 < len(words[i]):
        #             break
        #         elif self.is_predecessor(words[j], words[i]):
        #             result = max(result, dp[j] + 1)
        #     dp[i] = result
        # return max(dp)

        # Lee solution, great, O(n*s*s)
        #
        # dp = {}
        # for w in sorted(words, key=len):
        #     dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        # return max(dp.values())

        # I try to simplify it
        #
        # dp = {}
        # for w in sorted(words, key=len):
        #     result = 0
        #     for i in xrange(len(w)):
        #         result = max(result, dp.get(w[:i] + w[i + 1:], 0))
        #     dp[w] = result + 1
        # return max(dp.values())

        # solution from Babichev
        #
        # set_words = set(words)
        #
        # @lru_cache(None)
        # def dp(word):
        #     return max((dp(test) for i in range(len(word)) if (test := word[:i] + word[i+1:]) in set_words), default=0) + 1
        #
        # return max(dp(word) for word in words)

start_time = time()

_words = ["a","b","ba","bca","bda","bdca"]
# _words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# _words = ["a","b","ab","bac"]
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

print(Solution().longestStrChain(_words))

print("--- %s seconds ---" % (time() - start_time))
