from time import time


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = dict()
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in chars:
                chars[s[i]] = i
            else:
                chars[s[i]] = len(s)
        return -1 if min(chars.values()) == len(s) else min(chars.values())

        # official solution
        #
        # # build hash map : character and how often it appears
        # count = collections.Counter(s)
        #
        # # find the index
        # for idx, ch in enumerate(s):
        #     if count[ch] == 1:
        #         return idx
        # return -1


start_time = time()

_s = "vloveleetcode"
# Input: s = "loveleetcode"
# Output: 2

print(Solution().firstUniqChar(_s))

print("--- %s seconds ---" % (time() - start_time))
