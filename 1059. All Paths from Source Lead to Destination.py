from collections import defaultdict
from time import time
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # solution from comments

        g = defaultdict(set)
        visited = defaultdict(int)
        for [x, y] in edges:
            g[x].add(y)

        def dfs(node):
            if visited[node] == 1:
                return True
            elif visited[node] == -1:
                return False
            elif len(g[node]) == 0:
                return node == destination
            else:
                visited[node] = -1
                for child in g[node]:
                    if not dfs(child):
                        return False
                visited[node] = 1
                return True

        return dfs(source)

        # my solution, TLE
        #
        # graph = defaultdict(set)
        # for f, t in edges:
        #     graph[f].add(t)
        #
        # def dfs(cur, pred):
        #     if cur == destination:
        #         if graph[cur]:
        #             return False
        #         return True
        #     if not graph[cur]:
        #         return False
        #     for nxt in graph[cur]:
        #         if nxt in pred:
        #             return False
        #         if not dfs(nxt, pred | {cur}):
        #             return False
        #     return True
        #
        # return dfs(source, set())

start_time = time()

_n = 5
_edges = [[0,1],[0,2],[0,3],[0,3],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
_source = 0
_destination = 4

# _n = 4
# _edges = [[0,1],[0,2],[1,3],[2,3]]
# _source = 0
# _destination = 3
# Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
# Output: true

print(Solution().leadsToDestination(_n, _edges, _source,_destination))

print("--- %s seconds ---" % (time() - start_time))
