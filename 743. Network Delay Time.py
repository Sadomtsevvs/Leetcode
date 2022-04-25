from time import time
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        traces = defaultdict(list)
        for fr, to, ti in times:
            traces[fr].append((to, ti))
        nodes_visited = set()
        nodes_delay = {k: 0}
        next_nodes = [(k, 0)]
        while next_nodes:
            node, cur_time = next_nodes.pop()
            if node in nodes_visited:
                continue
            nodes_visited.add(node)
            for target, ti in traces[node]:
                if nodes_delay.get(target) is None:
                    nodes_delay[target] = cur_time + ti
                elif cur_time + ti < nodes_delay[target]:
                    nodes_delay[target] = cur_time + ti
                    nodes_visited -= {target}
                next_nodes.append((target, nodes_delay[target]))
        if len(nodes_visited) < n:
            return -1
        else:
            return max(nodes_delay.values())

        # Dijkstra's solution from LC comments
        #
        # graph = defaultdict(list)
        # for src, dst, c in times:
        #     graph[src].append((dst, c))
        #
        # queue = [(0, k)]  # (cost, node)
        # visited = set()
        # max_cost = 0
        #
        # while queue:
        #
        #     # Always pop the min value
        #     cost, node = heapq.heappop(queue)
        #
        #     if node in visited:
        #         continue
        #
        #     visited.add(node)
        #
        #     max_cost = max(max_cost, cost)
        #
        #     neighbours = graph[node]
        #
        #     for neighbour in neighbours:
        #
        #         new_node, new_cost = neighbour
        #
        #         if new_node not in visited:
        #             curr_cost = cost + new_cost
        #
        #             heapq.heappush(queue, (curr_cost, new_node))
        #
        # return max_cost if len(visited) == n else -1

        # from LC 2
        #
        # q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        # for u, v, w in times:
        #     adj[u].append((v, w))
        # while q:
        #     time, node = heapq.heappop(q)
        #     if node not in t:
        #         t[node] = time
        #         for v, w in adj[node]:
        #             heapq.heappush(q, (time + w, v))
        # return max(t.values()) if len(t) == N else -1


start_time = time()

_times = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],
          [4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
_n = 5
_k = 3
# Output 65
# Expected 59
print(Solution().networkDelayTime(_times, _n, _k))

print("--- %s seconds ---" % (time() - start_time))
