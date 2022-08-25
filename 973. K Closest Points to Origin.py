from time import time
from heapq import *


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [(point[0]**2 + point[1]**2, point) for point in points]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]

        # official solution
        #
        # points.sort(key=lambda P: P[0]**2 + P[1]**2)
        # return points[:K]


start_time = time()

_points = [[3,3],[5,-1],[-2,4]]
_k = 2
# _points = [[1, 3], [-2, 2]]
# _k = 1
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

print(Solution().kClosest(_points, _k))

print("--- %s seconds ---" % (time() - start_time))
