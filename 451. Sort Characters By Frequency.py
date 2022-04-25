import heapq
from time import time
from heapq import *
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        heapify(heap)
        for k, v in Counter(s).items():
            heappush(heap, (-v, k))
        result = ""
        while len(heap) > 0:
            n, c = heapq.heappop(heap)
            result += c*(-n)
        return result




start_time = time()

_s = "tree"
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

print(Solution().frequencySort(_s))

print("--- %s seconds ---" % (time() - start_time))
