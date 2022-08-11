from time import time
from collections import Counter, deque
import heapq


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        cntr_t = Counter(t)
        need_to_find = len(t)
        indexes = deque()
        len_ans = float('inf')
        ans = ''
        for i in range(len(s)):
            char = s[i]
            if char in cntr_t:
                indexes.append(i)
                if cntr_t[char] > 0:
                    need_to_find -= 1
                cntr_t[char] -= 1
                while cntr_t[s[indexes[0]]] < 0:
                    cntr_t[s[indexes.popleft()]] += 1
                if need_to_find == 0 and (i - indexes[0] + 1) < len_ans:
                    len_ans = i - indexes[0] + 1
                    ans = s[indexes[0]:i+1]
        return ans

        # cntr_t = Counter(t)
        # need_to_find = len(t)
        # heap = []
        # heapq.heapify(heap)
        # len_ans = float('inf')
        # ans = ''
        # for i in range(len(s)):
        #     char = s[i]
        #     if char in cntr_t:
        #         heapq.heappush(heap, i)
        #         if cntr_t[char] > 0:
        #             need_to_find -= 1
        #         cntr_t[char] -= 1
        #         while cntr_t[s[heap[0]]] < 0:
        #             cntr_t[s[heapq.heappop(heap)]] += 1
        #         if need_to_find == 0 and (i - heap[0] + 1) < len_ans:
        #             len_ans = i - heap[0] + 1
        #             ans = s[heap[0]:i+1]
        # return ans

        # solution from LC comments
        #
        # need, missing = Counter(t), len(t)
        # i = I = J = 0
        # for j, c in enumerate(s, 1):
        #     missing -= need[c] > 0
        #     need[c] -= 1
        #     if not missing:
        #         while i < j and need[s[i]] < 0:
        #             need[s[i]] += 1
        #             i += 1
        #         if not J or j - i <= J - I:
        #             I, J = i, j
        # return s[I:J]

start_time = time()

_s = "ADOBECODEBANC"
_t = "ABC"
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

print(Solution().minWindow(_s, _t))

print("--- %s seconds ---" % (time() - start_time))
