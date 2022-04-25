from time import time
from heapq import *


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        heap = []
        heapify(heap)
        for i in range(len(points)):
            px, py = points[i]
            if px == x:
                heappush(heap, (abs(py - y), i))
            elif py == y:
                heappush(heap, (abs(px - x), i))
        return -1 if not heap else heappop(heap)[1]


start_time = time()

_x = 3
_y = 4
_points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# Output: 2
# Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have
# the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

print(Solution().nearestValidPoint(_x, _y, _points))

print("--- %s seconds ---" % (time() - start_time))
