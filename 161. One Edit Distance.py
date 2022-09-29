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

        # official solution
        #
        # ns, nt = len(s), len(t)
        #
        # # Ensure that s is shorter than t.
        # if ns > nt:
        #     return self.isOneEditDistance(t, s)
        #
        # # The strings are NOT one edit away distance
        # # if the length diff is more than 1.
        # if nt - ns > 1:
        #     return False
        #
        # for i in range(ns):
        #     if s[i] != t[i]:
        #         # if strings have the same length
        #         if ns == nt:
        #             return s[i + 1:] == t[i + 1:]
        #         # if strings have different lengths
        #         else:
        #             return s[i:] == t[i + 1:]
        #
        # # If there is no diffs on ns distance
        # # the strings are one edit away only if
        # # t has one more character.
        # return ns + 1 == nt

        # from comments
        #
        # if s == t:
        #     return False
        # i = 0
        # while i < min(len(s),len(t)):
        #     if s[i] == t[i]:
        #         i += 1
        #     else:
        #         break
        # return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:]==t[i:]


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