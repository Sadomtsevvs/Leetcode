from time import time
from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        # if x == self.root[x]:
        #     return x
        # self.root[x] = self.find(self.root[x])
        # return self.root[x]
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)

        groups = {}

        for i in range(n):
            group = uf.find(i)
            if group in groups:
                groups[group] += 1
            else:
                groups[group] = 1

        groups = list(groups.values())

        result = 0
        prev_sum = 0
        for num in groups:
            result += prev_sum * num
            prev_sum += num

        # first solution, TLE
        # result = 0
        # for i in range(len(groups)-1):
        #     for j in range(i+1, len(groups)):
        #         result += i * j

        return result


start_time = time()

# Example 1:
# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
#
_n = 7
_edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Example 2:
# Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each other:
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
# Therefore, we return 14.

print(Solution().countPairs(_n, _edges))

print("--- %s seconds ---" % (time() - start_time))
