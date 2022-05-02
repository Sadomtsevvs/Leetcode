from time import time
import heapq
from collections import Counter, defaultdict


class Solution:
    def min_length_substring(self, s, t):
        cntr = Counter(t)
        all_idxs = []
        heapq.heapify(all_idxs)
        idxs = defaultdict(list)
        for key in cntr.keys():
            heap = []
            heapq.heapify(heap)
            idxs[key] = heap
        ans = len(s)
        cntr_is_empty = False
        for i in range(len(s)):
            if s[i] in cntr:
                if cntr[s[i]] > 0:
                    cntr[s[i]] -= 1
                else:
                    heapq.heappop(idxs[s[i]])
                    heapq.heappop(all_idxs)
                heapq.heappush(idxs[s[i]], i)
                heapq.heappush(all_idxs, i)
                if cntr_is_empty or all(not val for val in cntr.values()):
                    ans = min(ans, i - all_idxs[0] + 1)
                    cntr_is_empty = True
        return ans if cntr_is_empty else -1


start_time = time()

_s = "cbefebctrtrttrte"
_t = "fd"
# Example
# s = "dcbefebce"
# t = "fd"
# output = 5
# Explanation:
# Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.

print(Solution().min_length_substring(_s, _t))

print("--- %s seconds ---" % (time() - start_time))
