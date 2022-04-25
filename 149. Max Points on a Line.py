from time import time


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        # i know that it's not efficient
        result = 1
        for i in range(len(points) - 1):
            coeff = {}
            for j in range(i + 1, len(points)):
                if points[j][0] == points[i][0]:
                    k = None
                    b = points[i][0]
                else:
                    k = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    b = points[i][1] - k * points[i][0]
                if (k, b) in coeff:
                    coeff[(k, b)] += 1
                else:
                    coeff[(k, b)] = 2
            result = max(result, max(coeff.values()))
        return result


start_time = time()

_points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

print(Solution().maxPoints(_points))

print("--- %s seconds ---" % (time() - start_time))
