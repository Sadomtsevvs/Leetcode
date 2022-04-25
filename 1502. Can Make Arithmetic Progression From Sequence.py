from time import time
from heapq import *


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        heapify(arr)
        first, second = heappop(arr), heappop(arr)
        delta = first - second
        while arr:
            first, second = second, heappop(arr)
            if first - second != delta:
                return False
        return True


start_time = time()

_arr = [3,5,1]
_arr = [1,2,4]
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

print(Solution().canMakeArithmeticProgression(_arr))

print("--- %s seconds ---" % (time() - start_time))
