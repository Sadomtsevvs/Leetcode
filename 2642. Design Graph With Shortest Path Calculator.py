from collections import defaultdict
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.paths = defaultdict(list)
        for frm, to, cost in edges:
            self.paths[frm].append([to, cost])

    def addEdge(self, edge: List[int]) -> None:
        frm, to, cost = edge
        self.paths[frm].append([to, cost])

    def shortestPath(self, node1: int, node2: int) -> int:
        min_paths = dict()
        min_paths[node1] = 0
        nodes = [node1]
        while nodes:
            node = nodes.pop()
            for next_node, cost in self.paths[node]:
                if next_node in min_paths:
                    if min_paths[next_node] > min_paths[node] + cost:
                        min_paths[next_node] = min_paths[node] + cost
                        nodes.append(next_node)
                else:
                    min_paths[next_node] = min_paths[node] + cost
                    nodes.append(next_node)
        return -1 if node2 not in min_paths else min_paths[node2]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)