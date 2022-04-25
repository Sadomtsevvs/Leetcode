from time import time


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        rules1, rules2 = {}, {}
        for p, w in zip(pattern, words):
        # for i in range(len(pattern)):
            if p not in rules1 and w not in rules2:
                rules1[p] = w
                rules2[w] = p
            elif p in rules1 and rules1[p] != w:
                return False
            elif w in rules2 and rules2[w] != p:
                return False
        return True

        # interesting zip solution from LC comments
        #
        # mapping = {}
        # inv_mapping = {}
        # split = s.split()
        # if len(pattern) != len(split):
        #     return False
        # for c, w in zip(pattern, split):
        #     if c in mapping and w != mapping[c] or w in inv_mapping and c != inv_mapping[w]:
        #         return False
        #     else:
        #         mapping[c] = w
        #         inv_mapping[w] = c
        # return True

start_time = time()

_pattern = "abba"
_s = "dog cat cat dog"
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

print(Solution().wordPattern(_pattern, _s))

print("--- %s seconds ---" % (time() - start_time))