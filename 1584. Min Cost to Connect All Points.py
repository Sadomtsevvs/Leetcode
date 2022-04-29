from time import time
from heapq import *


# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        # Kruskal algorithm
        #
        # heap = []
        # heapify(heap)
        # for p1 in range(len(points) - 1):
        #     for p2 in range(p1 + 1, len(points)):
        #         heappush(heap, (abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1]), p1, p2))
        # result = 0
        # cnt = 0
        # uf = UnionFind(len(points))
        # while heap and cnt < len(points) - 1:
        #     cost, p1, p2 = heappop(heap)
        #     if not uf.connected(p1, p2):
        #         uf.union(p1, p2)
        #         result += cost
        #         cnt += 1
        # return result

        # Prim algorithm
        #
        heap = []
        heapify(heap)
        for p2 in range(1, len(points)):
            heappush(heap, (abs(points[0][0] - points[p2][0]) + abs(points[0][1] - points[p2][1]), 0, p2))
        visited = {0}
        result = 0
        while len(visited) < len(points):
            cost, p1, p2 = heappop(heap)
            p = p2 if p2 not in visited else p1
            if p not in visited:
                result += cost
                visited.add(p)
                for next_p in range(0, len(points)):
                    if next_p not in visited:
                        heappush(heap, (abs(points[p][0] - points[next_p][0]) +
                                        abs(points[p][1] - points[next_p][1]),
                                        p, next_p))
        return result


start_time = time()

_points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# _points = [[2,-3],[-17,-8],[13,8],[-17,-15]]
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

print(Solution().minCostConnectPoints(_points))

print("--- %s seconds ---" % (time() - start_time))
