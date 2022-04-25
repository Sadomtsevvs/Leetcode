# from functools import reduce
from time import time
from heapq import *


class Solution:
    def findMaxProduct(self, arr):
        # result = []
        # heap = []
        # heapify(heap)
        # for a in arr:
        #     heappush(heap, a)
        #     if len(heap) < 3:
        #         result.append(-1)
        #     else:
        #         result.append(reduce(lambda x, y: x*y, nlargest(3, heap)))
        # return result

        result = []
        heap = []
        heapify(heap)
        for a in arr:
            if len(heap) < 2:
                heappush(heap, a)
                result.append(-1)
                continue
            if len(heap) < 3:
                heappush(heap, a)
            elif a > heap[0]:
                heapreplace(heap, a)
            result.append(heap[0] * heap[1] * heap[2])

        return result


start_time = time()

_arr = [1, 2, 3, 4, 5]
# n = 5
# arr = [1, 2, 3, 4, 5]
# output = [-1, -1, 6, 24, 60]
# The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24, and the 5th is 5*4*3 = 60.

print(Solution().findMaxProduct(_arr))

print("--- %s seconds ---" % (time() - start_time))
