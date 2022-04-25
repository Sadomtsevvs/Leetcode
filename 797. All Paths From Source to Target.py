from time import time
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:

        # my first solution
        #
        # result = []
        #
        # def findpath(path, node_index):
        #     if node_index == len(graph) - 1:
        #         result.append(path)
        #     for next_node_index in graph[node_index]:
        #         findpath(path + [next_node_index], next_node_index)
        #
        # findpath([0], 0)
        #
        # return result

        # my bfs solution

        result = []

        queue = deque([[0]])
        while queue:
            path = queue.popleft()
            if path[-1] == len(graph) - 1:
                result.append(path)
            for next_el in graph[path[-1]]:
                queue.append(path + [next_el])
        return result

        # solution from comments without recursion
        #
        # def allPathsSourceTarget(graph):
        #
        #     # edges cases:
        #     if not graph:
        #         return []
        #
        #     # build di-graph
        #     d = {}
        #     for i in range(len(graph)):
        #         d[i] = graph[i]  # one-way link
        #
        #     # apply DFS on DAG
        #     n = len(graph)
        #     stack = [(0, [0])]  # - store noth the (node, and the path leading to it)
        #     res = []
        #     while stack:
        #         node, path = stack.pop()
        #         # check leaf
        #         if node == n - 1:
        #             res.append(path)
        #         # traverse rest
        #         for nei in d[node]:
        #             stack.append((nei, path + [nei]))
        #     return res

start_time = time()

_graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

print(Solution().allPathsSourceTarget(_graph))

print("--- %s seconds ---" % (time() - start_time))
