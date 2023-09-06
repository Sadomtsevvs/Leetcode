import heapq
from collections import defaultdict
from time import time


class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = defaultdict(int)
        for char in s:
            chars[char] += 1
        h = []
        heapq.heapify(h)
        for k, v in chars.items():
            heapq.heappush(h, (-v, k))
        if -h[0][0] > (len(s) // 2 + len(s) % 2):
            return ""
        ans = ''
        while len(ans) < len(s):
            n1, char1 = heapq.heappop(h)
            ans += char1
            if h:
                n2, char2 = heapq.heappop(h)
                ans += char2
                if n2 != -1:
                    heapq.heappush(h, (n2+1, char2))
            if n1 != -1:
                heapq.heappush(h, (n1+1, char1))
        return ans


start_time = time()

# Example 1:
# Input: s = "aab"
_s = "aab"
# Output: "aba"
#
# Example 2:
# Input: s = "aaab"
# Output: ""

print(Solution().reorganizeString(_s))

print("--- %s seconds ---" % (time() - start_time))
