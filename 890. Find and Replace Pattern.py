from time import time
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            pat_word = dict()
            dic_word = dict()
            for i in range(len(word)):
                if pattern[i] in pat_word and pat_word[pattern[i]] != word[i]:
                    break
                if word[i] in dic_word and dic_word[word[i]] != pattern[i]:
                    break
                if pattern[i] not in pat_word:
                    pat_word[pattern[i]] = word[i]
                    dic_word[word[i]] = pattern[i]
            else:
                result.append(word)
        return result

        # official solution
        #
        # def match(word):
        #     m1, m2 = {}, {}
        #     for w, p in zip(word, pattern):
        #         if w not in m1: m1[w] = p
        #         if p not in m2: m2[p] = w
        #         if (m1[w], m2[p]) != (p, w):
        #             return False
        #     return True
        #
        # return filter(match, words)

        # Lee solution
        #
        # def F(w):
        #     m = {}
        #     return [m.setdefault(c, len(m)) for c in w]
        # return [w for w in words if F(w) == F(p)]


start_time = time()

_words = ["abc","deq","mee","aqq","dkd","ccc"]
_pattern = "abb"
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

print(Solution().findAndReplacePattern(_words, _pattern))

print("--- %s seconds ---" % (time() - start_time))
