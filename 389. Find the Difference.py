from time import time
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]

        # from LC comments 1
        #
        # c = 0
        # for cs in s: c ^= ord(cs) #ord is ASCII value
        # for ct in t: c ^= ord(ct)
        # return chr(c) #chr = convert ASCII into character

        # from LC comments 2
        #
        # return chr(reduce(lambda x, y: x ^ y, map(ord, s + t)))


start_time = time()

_s = "abcd"
_t = "abcde"
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.

print(Solution().findTheDifference(_s, _t))

print("--- %s seconds ---" % (time() - start_time))
