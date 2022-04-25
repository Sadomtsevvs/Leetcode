from time import time
from collections import defaultdict

# UnionFind class
class UnionFind:
    def __init__(self, num):
        self.root = list(range(num))
        self.rank = list(range(num))

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


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        # disjoint solution

        # u = UnionFind(n)
        # for edge_from, edge_to in edges:
        #     u.union(edge_from, edge_to)
        # return u.find(source) == u.find(destination)

        # bfs solution

        adjacency_list = defaultdict(list)
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        visited = set()

        queue = [source]
        while queue:
            next_queue = []
            for el_from in queue:
                if el_from == destination:
                    return True
                visited.add(el_from)
                for el_to in adjacency_list[el_from]:
                    if el_to not in visited:
                        next_queue.append(el_to)
            queue = next_queue
        return False

        # too slow
        #
        # def dfs(last, visited):
        #     if last == destination:
        #         return True
        #     for edge1, edge2 in edges:
        #         if edge1 == last and edge2 not in visited:
        #             if dfs(edge2, visited | {edge2}):
        #                 return True
        #         if edge2 == last and edge1 not in visited:
        #             if dfs(edge1, visited | {edge1}):
        #                 return True
        #     return False
        #
        # return dfs(source, {source})

        # official solution
        #
        # adjacency_list = [[] for _ in range(n)]
        # for a, b in edges:
        #     adjacency_list[a].append(b)
        #     adjacency_list[b].append(a)
        #
        # stack = [start]
        # seen = set()
        #
        # while stack:
        #     # Get the current node.
        #     node = stack.pop()
        #
        #     # Check if we have reached the target node.
        #     if node == end:
        #         return True
        #
        #     # Check if we've already visited this node.
        #     if node in seen:
        #         continue
        #     seen.add(node)
        #
        #     # Add all neighbors to the stack.
        #     for neighbor in adjacency_list[node]:
        #         stack.append(neighbor)
        #
        # # Our stack is empty and we did not reach the end node.
        # return False


start_time = time()

_n = 100
_edges = [[3,12],[26,84],[10,43],[68,47],[33,10],[87,35],[41,96],[70,92],[38,31],[88,59],[7,30],[89,26],[95,25],[66,28],
          [14,24],[86,11],[83,65],[14,4],[67,7],[89,45],[52,73],[47,85],[86,53],[68,81],[43,68],[87,78],[94,49],[70,21],
          [11,82],[60,93],[22,32],[69,99],[7,1],[41,46],[73,94],[98,52],[68,0],[69,89],[37,72],[25,50],[72,78],[96,60],
          [73,95],[7,69],[97,19],[46,75],[8,38],[19,36],[64,41],[61,78],[97,14],[54,28],[6,18],[25,32],[34,77],[58,60],
          [17,63],[98,87],[13,76],[58,53],[81,74],[29,6],[37,5],[65,63],[89,56],[61,18],[23,34],[76,29],[73,76],[11,63],
          [98,0],[54,14],[63,7],[87,32],[79,57],[72,0],[94,16],[85,16],[12,91],[14,17],[30,45],[42,41],[82,69],[24,28],
          [31,59],[11,88],[41,89],[48,12],[92,76],[84,64],[19,64],[21,32],[30,19],[47,43],[45,27],[31,17],[53,36],
          [88,3],[83,7],[27,48],[13,6],[14,40],[90,28],[80,85],[29,79],[10,50],[56,86],[82,88],[11,99],[37,55],[62,2],
          [55,92],[51,53],[9,40],[65,97],[25,57],[7,96],[86,1],[39,93],[45,86],[40,90],[58,75],[99,86],[82,45],[5,81],
          [89,91],[15,83],[93,38],[3,93],[71,28],[11,97],[74,47],[64,96],[88,96],[4,99],[88,26],[0,55],[36,75],[26,24],
          [84,88],[58,40],[77,72],[58,48],[50,92],[62,68],[70,49],[41,71],[68,6],[64,91],[50,81],[35,44],[91,48],
          [21,37],[62,98],[64,26],[63,51],[77,55],[25,13],[60,41],[87,79],[75,17],[61,95],[30,82],[47,79],[28,7],
          [92,95],[91,59],[94,85],[24,65],[91,31],[3,9],[59,58],[70,43],[95,13],[30,96],[51,9],[16,70],[29,94],[37,22],
          [35,79],[14,90],[75,9],[2,57],[81,80],[61,87],[69,88],[98,79],[18,70],[82,19],[36,27],[49,62],[67,75],[62,77],
          [83,96],[92,37],[95,22],[46,97],[35,0],[44,79],[82,89],[68,94],[96,31],[92,34],[25,0],[46,36],[38,84],[21,0],
          [0,80],[72,44],[56,97],[86,26],[94,57],[25,6],[81,13],[66,63],[57,5],[72,49],[46,86],[95,16],[95,37],[14,89],
          [44,22],[60,39],[37,47],[58,86],[89,96],[38,83],[51,91],[72,70],[14,82],[60,30],[58,39],[57,22],[95,70],
          [44,76],[5,68],[15,69],[33,61],[81,32],[21,68],[73,20],[22,72],[83,8],[15,54],[93,42],[68,95],[55,72],[33,92],
          [5,49],[17,96],[44,77],[24,53],[2,98],[33,81],[32,43],[20,16],[67,84],[98,35],[58,11],[72,5],[3,59],[78,79],
          [6,0],[26,71],[96,97],[18,92],[1,36],[78,0],[63,15],[20,43],[32,73],[37,76],[73,16],[76,23],[50,44],[68,2],
          [14,86],[69,65],[95,98],[53,64],[6,76],[7,11],[14,84],[62,50],[83,58],[78,92],[37,0],[13,55],[12,86],[11,59],
          [41,86],[27,26],[94,43],[20,78],[0,73],[58,90],[69,36],[62,34],[65,26],[32,85]]
_source = 20
_destination = 53

# _n = 6
# _edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# _source = 0
# _destination = 5
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

print(Solution().validPath(_n, _edges, _source, _destination))

print("--- %s seconds ---" % (time() - start_time))
