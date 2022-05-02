from time import time
from collections import defaultdict


class Solution:
    def matching_pairs(self, s, t):
        ans = 0
        mapping = defaultdict(set)
        for i in range(len(s)):
            if s[i] == t[i]:
                ans += 1
            else:
                mapping[s[i]].add(t[i])
        if not mapping:
            # if there are no pair symbols we have to swap any 2 elements
            if len(s) == len(set(s)):
                return ans - 2
            # if there are pair symbols we can swap them and nothing changes
            else:
                return ans
        for s_i, set_t in mapping.items():
            for t_j in set_t:
                if mapping.get(t_j) is not None and s_i in mapping[t_j]:
                    return ans + 2
        return ans


start_time = time()

_s = "abcd"
_t = "adcb"
_s = "mno"
_t = "mnc"
# Example 1
# s = "abcd"
# t = "adcb"
# output = 4
# Explanation:
# Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
# Therefore, the number of matching pairs of s and t will be 4.

print(Solution().matching_pairs(_s, _t))

print("--- %s seconds ---" % (time() - start_time))
