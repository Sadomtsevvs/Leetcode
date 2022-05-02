# from functools import reduce
import heapq
from time import time


class Solution:
    def maxCandies(self, arr, k):
        heap = []
        heapq.heapify(heap)
        for a in arr:
            heapq.heappush(heap, -a)
        ans = 0
        for i in range(k):
            candy = -heapq.heappop(heap)
            ans += candy
            heapq.heappush(heap, -(candy//2))
        return ans


start_time = time()

_arr = [2, 1, 7, 4, 2]
_k = 3
# N = 5
# k = 3
# arr = [2, 1, 7, 4, 2]
# output = 14
# In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
# In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
# In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
# In total you can eat 7 + 4 + 3 = 14 pieces of candy.

print(Solution().maxCandies(_arr, _k))

print("--- %s seconds ---" % (time() - start_time))
