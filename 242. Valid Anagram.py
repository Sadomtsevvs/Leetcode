from time import time
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = Counter(s)
        counter_t = Counter(t)
        for key, value in counter_s.items():
            if value > counter_t[key]:
                return False
        return True

        # shorter solution from LC comments
        #
        # if len(s) != len(t):
        #     return False
        # return Counter(s) == Counter(t)

start_time = time()

_s = "rat"
_t = "car"
# Input: s = "anagram", t = "nagaram"
# Output: true

print(Solution().isAnagram(_s, _t))

print("--- %s seconds ---" % (time() - start_time))