from time import time
from heapq import *


class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        heap = [(bin(num).count('1'), num) for num in arr]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(len(arr))]

        # from LC comments
        #
        # return sorted(A, key=lambda a: [bin(a).count('1'), a])


start_time = time()

_arr = [0,1,2,3,4,5,6,7,8]
_arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]

print(Solution().sortByBits(_arr))

print("--- %s seconds ---" % (time() - start_time))
