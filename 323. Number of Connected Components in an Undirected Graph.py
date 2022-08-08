from typing import List


class UnionFind:

    def __init__(self, n):
        self.uf = list(range(n))
        self.rank = [1] * n

    def find(self, n):
        if self.uf[n] == n:
            return n
        self.uf[n] = self.find(self.uf[n])
        return self.uf[n]

    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)

    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.uf[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.uf[root1] = root2
        else:
            self.uf[root2] = root1
            self.rank[root1] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)

        roots = set()
        for i in range(n):
            roots.add(uf.find(i))

        return len(roots)
