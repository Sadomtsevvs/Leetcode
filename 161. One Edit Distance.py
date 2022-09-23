from time import time


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if abs(len_s - len_t) > 1:
            return False
        point_s = 0
        point_t = 0
        have_diff = False
        while point_s < len_s or point_t < len_t:
            if point_s < len_s and point_t < len_t and s[point_s] == t[point_t]:
                point_s += 1
                point_t += 1
            elif have_diff:
                return False
            else:
                if len_s == len_t:
                    point_s += 1
                    point_t += 1
                elif len_s < len_t:
                    point_t += 1
                else:
                    point_s += 1
                have_diff = True
        return have_diff


start_time = time()

_s = "ab"
_t = "acb"
# Example 1:
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
#
# Example 2:
# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.

print(Solution().isOneEditDistance(_s, _t))

print("--- %s seconds ---" % (time() - start_time))