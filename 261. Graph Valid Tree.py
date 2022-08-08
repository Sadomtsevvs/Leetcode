# UnionFind class
from typing import List


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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        uf = UnionFind(n)

        # check for cycles
        for node1, node2 in edges:
            if uf.connected(node1, node2):
                return False
            uf.union(node1, node2)

        # check for fully connected
        for i in range(1, n):
            if not uf.connected(0, i):
                return False

        return True

        # BFS solution after reading official
        #
        # dic = defaultdict(set)
        #
        # for node1, node2 in edges:
        #     dic[node1].add(node2)
        #     dic[node2].add(node1)
        #
        # seen = {0}
        # nodes = [0]
        # while nodes:
        #     next_nodes = []
        #     for node in nodes:
        #         for adj in dic[node]:
        #             if adj in seen:
        #                 return False
        #             seen.add(adj)
        #             dic[adj].remove(node)
        #             next_nodes.append(adj)
        #     nodes = next_nodes
        # return len(seen) == n