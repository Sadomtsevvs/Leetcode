from time import time


# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.count = size

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
            self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        # my first solution, works
        #
        # result = 0
        # marked = set()
        #
        # def mark_neighbours(i):
        #     neighbours = [i]
        #     while neighbours:
        #         neighbour = neighbours.pop()
        #         for j in range(0, len(isConnected)):
        #             if j in marked:
        #                 continue
        #             if isConnected[neighbour][j] == 1:
        #                 marked.add(j)
        #                 neighbours.append(j)
        #
        # for i in range(len(isConnected)):
        #     if i in marked:
        #         continue
        #     marked.add(i)
        #     mark_neighbours(i)
        #     result += 1
        #
        # return result

        # solution using graph
        #
        my_union = UnionFind(len(isConnected))
        for i in range(len(isConnected)-1):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    my_union.union(i, j)
        return my_union.count

start_time = time()

_isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]

print(Solution().findCircleNum(_isConnected))

print("--- %s seconds ---" % (time() - start_time))
