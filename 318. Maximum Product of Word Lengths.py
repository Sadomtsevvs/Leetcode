from time import time
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # ans = 0
        # set_words = [set(word) for word in words]
        # for i in range(len(words) - 1):
        #     for j in range(i+1, len(words)):
        #         if not set_words[i] & set_words[j]:
        #             ans = max(ans, len(words[i]) * len(words[j]))
        # return ans

        # from LC
        #
        # def common(chars1, chars2):
        #     for c1, c2 in zip(chars1, chars2):
        #         if c1 and c2: return True
        #     return False
        #
        # chars, ans = [[False] * 26 for i in range(len(words))], 0
        # for i, word in enumerate(words):
        #     for ch in word:
        #         chars[i][ord(ch) - ord('a')] = True
        #     for j in range(i):
        #         if not common(chars[i], chars[j]):
        #             ans = max(ans, len(words[i]) * len(words[j]))
        # return ans

        # from LC
        #
        # mask, ans = [0] * len(words), 0
        # for i, word in enumerate(words):
        #     for ch in word:
        #         mask[i] |= 1 << (ord(ch) - ord('a'))
        #     for j in range(i):
        #         if not mask[i] & mask[j]:
        #             ans = max(ans, len(words[i]) * len(words[j]))
        # return ans

        # from LC
        #
        # d, ans = defaultdict(int), 0
        # for word in words:
        #     for l in word:
        #         d[word] |= 1 << (ord(l) - 97)
        # for w1, w2 in combinations(d.keys(), 2):
        #     if d[w1] & d[w2] == 0:
        #         ans = max(ans, len(w1) * len(w2))
        # return ans


start_time = time()

_words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# _words = ["a","ab","abc","d","cd","bcd","abcd"]
# _words = ["a","aa","aaa","aaaa"]
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

print(Solution().maxProduct(_words))

print("--- %s seconds ---" % (time() - start_time))
