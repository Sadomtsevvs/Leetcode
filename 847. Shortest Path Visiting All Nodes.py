from collections import defaultdict, deque, namedtuple
from time import time
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        #
        # # correct, but TLE
        #
        # def dfs(cur, visited, forbidden, length):
        #     visited.add(cur)
        #     if len(visited) == len(graph):
        #         return length
        #     res = float('inf')
        #     for nxt in graph[cur]:
        #         if nxt in forbidden[cur]:
        #             continue
        #         forbidden[cur].add(nxt)
        #         visited_before = visited.copy()
        #         res = min(res, dfs(nxt, visited, forbidden, length + 1))
        #         visited = visited_before
        #         forbidden[cur].remove(nxt)
        #     return res
        #
        # ans = float('inf')
        # for i in range(len(graph)):
        #     ans = min(ans, dfs(i, set(),  defaultdict(set), 0))
        # return ans

        # from comments

        n = len(graph)
        all_mask = (1 << n) - 1
        visited = set()
        Node = namedtuple('Node', ['node', 'mask', 'cost'])

        q = deque()
        for i in range(n):
            mask_value = (1 << i)
            this_node = Node(i, mask_value, 1)
            q.append(this_node)
            visited.add((i, mask_value))

        while q:
            curr = q.popleft()

            if curr.mask == all_mask:
                return curr.cost - 1

            for adj in graph[curr.node]:
                both_visited_mask = curr.mask | (1 << adj)
                this_node = Node(adj, both_visited_mask, curr.cost + 1)

                if (adj, both_visited_mask) not in visited:
                    visited.add((adj, both_visited_mask))
                    q.append(this_node)

        return -1


start_time = time()

# Example 1:
# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
#
# Example 2:
# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# _graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
_graph = [[1,5],[0,3],[3,5],[1,2,5],[7],[0,7,6,2,3],[5],[5,4,8],[7]]
_graph = [[2,10],[2,7],[0,1,3,4,5,8],[2],[2],[2],[8],[9,11,8,1],[7,6,2],[7],[11,0],[7,10]]

print(Solution().shortestPathLength(_graph))

print("--- %s seconds ---" % (time() - start_time))
