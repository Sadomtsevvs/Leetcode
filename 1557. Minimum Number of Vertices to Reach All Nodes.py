from time import time


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        result = set(range(n))
        for (begin, end) in edges:
            result -= {end}
        return list(result)


start_time = time()

_n = 6
_edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

print(Solution().findSmallestSetOfVertices(_n, _edges))

print("--- %s seconds ---" % (time() - start_time))
