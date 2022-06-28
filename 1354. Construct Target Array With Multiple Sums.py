from time import time
from typing import List
from heapq import *


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = 0
        heap = []
        for t in target:
            heappush(heap, -t)
            s += t
        while s != len(target):
            biggest = -heappop(heap)
            s -= biggest
            if s == 1:
                return True
            if s == 0 or biggest <= s:
                return False
            new = biggest % s
            if new == 0:
                return False
            heappush(heap, -new)
            s += new
        return True


start_time = time()

_target = [9, 3, 5]
# _target = [1,1,1,2]
_target = [8,5]
_target = [1,1000000000]
# _target = [2,900000001]
# _target = [2]
# Input: target = [9,3,5]
# Output: true
# Explanation: Start with arr = [1, 1, 1]
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done

print(Solution().isPossible(_target))

print("--- %s seconds ---" % (time() - start_time))