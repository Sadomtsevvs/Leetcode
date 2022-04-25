from time import time


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        rools_st = dict()
        rools_ts = dict()
        for i in range(len(s)):
            if s[i] in rools_st:
                if rools_st[s[i]] != t[i]:
                    return False
            elif t[i] in rools_ts:
                if rools_ts[t[i]] != s[i]:
                    return False
            else:
                rools_st[s[i]] = t[i]
                rools_ts[t[i]] = s[i]
        return True


start_time = time()

_s = "paper"
_t = "title"
_s = "bar"
_t = "foo"
# Input: s = "paper", t = "title"
# Output: true

print(Solution().isIsomorphic(_s, _t))

print("--- %s seconds ---" % (time() - start_time))
