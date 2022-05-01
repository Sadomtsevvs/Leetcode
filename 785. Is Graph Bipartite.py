from time import time
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        first_partie = set()
        second_partie = set()
        to_visit = set(range(1, len(graph)))
        stack = [0]
        while stack or to_visit:
            if stack:
                i = stack.pop()
            else:
                i = to_visit.pop()
            if i in first_partie:
                part_i = 1
            elif i in second_partie:
                part_i = 2
            else:
                first_partie.add(i)
                part_i = 1
            for conn in graph[i]:
                if part_i == 1:
                    if conn in first_partie:
                        return False
                    if conn not in second_partie:
                        second_partie.add(conn)
                else:
                    if conn in second_partie:
                        return False
                    if conn not in first_partie:
                        first_partie.add(conn)
                if conn in to_visit:
                    stack.append(conn)
                    to_visit.remove(conn)
        return True

        # Lee solution
        #
        # color = {}
        # def dfs(pos):
        #     for i in graph[pos]:
        #         if i in color:
        #             if color[i] == color[pos]:
        #                 return False
        #         else:
        #             color[i] = 1 - color[pos]
        #             if not dfs(i):
        #                 return False
        #     return True
        # for i in range(len(graph)):
        #     if i not in color:
        #         color[i] = 0
        #         if not dfs(i):
        #             return False
        # return True

        # another solution, bfs
        #
        # n, colored = len(graph), {}
        # for i in range(n):
        #     if i not in colored and graph[i]:
        #         colored[i] = 1
        #         q = collections.deque([i])
        #         while q:
        #             cur = q.popleft()
        #             for nb in graph[cur]:
        #                 if nb not in colored:
        #                     colored[nb] = -colored[cur]
        #                     q.append(nb)
        #                 elif colored[nb] == colored[cur]:
        #                     return False
        # return True


start_time = time()

_graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
_graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
# _graph = [[1,3],[0,2],[1,3],[0,2]]
# _graph = [[1],[0,3],[3],[1,2]]
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

print(Solution().isBipartite(_graph))

print("--- %s seconds ---" % (time() - start_time))
