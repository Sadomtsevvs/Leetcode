import heapq
from time import time


class Solution:
    def findMedian(self, arr):
        minheap, maxheap = [], []
        heapq.heapify(minheap)
        heapq.heapify(maxheap)
        ans = []
        for a in arr:
            if len(maxheap) == len(minheap):
                if not minheap or a >= minheap[0]:
                    heapq.heappush(minheap, a)
                    ans.append(minheap[0])
                else:
                    heapq.heappush(maxheap, -a)
                    ans.append(-maxheap[0])
            elif len(minheap) > len(maxheap):
                if a >= minheap[0]:
                    heapq.heappush(minheap, a)
                    heapq.heappush(maxheap, -heapq.heappop(minheap))
                else:
                    heapq.heappush(maxheap, -a)
                ans.append((-maxheap[0]+minheap[0])//2)
            else:
                if a < maxheap[0]:
                    heapq.heappush(maxheap, -a)
                    heapq.heappush(minheap, -heapq.heappop(maxheap))
                else:
                    heapq.heappush(minheap, a)
                ans.append((-maxheap[0]+minheap[0])//2)
        return ans

start_time = time()

_arr = [5, 15, 1, 3]
# n = 4
# arr = [5, 15, 1, 3]
# output = [5, 10, 5, 4]
# The median of [5] is 5, the median of [5, 15] is (5 + 15) / 2 = 10, the median of [5, 15, 1] is 5, and the median of [5, 15, 1, 3] is (3 + 5) / 2 = 4.

print(Solution().findMedian(_arr))

print("--- %s seconds ---" % (time() - start_time))
