from copy import deepcopy
from time import time
from typing import List


class UnionFind:
    def __init__(self, n):
        self.distinct = n
        self.root = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def connect(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 0
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        self.distinct -= 1
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        required = 0

        alice = UnionFind(n)
        # bob = UnionFind(n)

        for t, u, v in edges:
            if t == 3:
                required += alice.connect(u, v)
                # bob.connect(u, v)

        bob = deepcopy(alice)

        for t, u, v in edges:
            if t == 1:
                required += alice.connect(u, v)
            elif t == 2:
                required += bob.connect(u, v)

        if alice.distinct == 1 and bob.distinct == 1:
            return len(edges) - required

        return -1


start_time = time()

# Example 1:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
_n = 4
_edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
#
# Example 2:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
#
# Example 3:
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.


print(Solution().maxNumEdgesToRemove(_n, _edges))

print("--- %s seconds ---" % (time() - start_time))
