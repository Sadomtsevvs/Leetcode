from time import time
from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # solution from LC
        #
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n

        # dfs function returns the minimum rank it finds

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n  # initial rank, max value
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
                neighbor_depth = dfs(neighbor, depth + 1)
                if neighbor_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, neighbor_depth)
            # rank[node] = n  # this line is not necessary. see the "brain teaser" section below
            return min_back_depth

        dfs(0, 0)
        return list(connections)


        # my solution, TLE
        #
        # d = defaultdict(set)
        # for x, y in connections:
        #     d[x].add(y)
        #     d[y].add(x)
        #
        # def connected(xx, yy):
        #     seen = {xx}
        #     stack = [xx]
        #     while stack:
        #         node = stack.pop()
        #         for dx in d[node]:
        #             if dx not in seen:
        #                 seen.add(dx)
        #                 stack.append(dx)
        #     return yy in seen
        #
        # result = []
        # for x, y in connections:
        #     d[x].remove(y)
        #     d[y].remove(x)
        #     if not connected(x, y):
        #         result.append([x, y])
        #     d[x].add(y)
        #     d[y].add(x)
        # return result


start_time = time()

_n = 4
_connections = [[0,1],[1,2],[2,0],[1,3]]
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

print(Solution().criticalConnections(_n, _connections))

print("--- %s seconds ---" % (time() - start_time))
