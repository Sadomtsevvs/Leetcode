import time
from collections import defaultdict
import heapq


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        ancs = defaultdict(set)
        for edge in edges:
            ancs[edge[1]].add(edge[0])
        result = defaultdict(set)
        for i in range(n):
            h = []
            seen = {i}
            nexts = [i]
            while nexts:
                next = nexts.pop()
                for anc in ancs[next]:
                    if anc not in seen:
                        heapq.heappush(h, anc)
                        nexts.append(anc)
                        seen.add(anc)
            result[i] = [heapq.heappop(h) for _ in range(len(h))]
        return list(result.values())


# _n = 8
# _edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
_n = 6
_edges = [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]
# Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
# Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
# Explanation:
# The above diagram represents the input graph.
# - Nodes 0, 1, and 2 do not have any ancestors.
# - Node 3 has two ancestors 0 and 1.
# - Node 4 has two ancestors 0 and 2.
# - Node 5 has three ancestors 0, 1, and 3.
# - Node 6 has five ancestors 0, 1, 2, 3, and 4.
# - Node 7 has four ancestors 0, 1, 2, and 3.

print(Solution().getAncestors(_n, _edges))
