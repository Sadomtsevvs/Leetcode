from time import time
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts += [0, h]
        verticalCuts += [0, w]
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = 0
        for i in range(len(horizontalCuts)-1):
            max_h = max(max_h, horizontalCuts[i+1] - horizontalCuts[i])
        max_v = 0
        for i in range(len(verticalCuts)-1):
            max_v = max(max_v, verticalCuts[i+1] - verticalCuts[i])
        return (max_h * max_v) % (10**9 + 7)


start_time = time()

_h = 5
_w = 4
_horizontalCuts = [1,2,4]
_verticalCuts = [1,3]
_h = 5
_w = 4
_horizontalCuts = [3,1]
_verticalCuts = [1]
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts.
# After you cut the cake, the green piece of cake has the maximum area.

print(Solution().maxArea(_h, _w, _horizontalCuts, _verticalCuts))

print("--- %s seconds ---" % (time() - start_time))
