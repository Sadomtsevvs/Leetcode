from collections import defaultdict
from time import time
from typing import List
import heapq


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        paths = defaultdict(list)
        for node1, node2 in edges:
            paths[node1].append(node2)
            paths[node2].append(node1)
        influenses = [0] * n
        for start, target in trips:
            seen = set()
            nxt = [(start, [start])]
            while nxt:
                node, path = nxt.pop()
                seen.add(node)
                if node == target:
                    for point in path:
                        influenses[point] += price[point]
                    break
                for follow in paths[node]:
                    if follow not in seen:
                        nxt.append((follow, path+[follow]))
        answer = sum(influenses)
        influenses = [(el*(-1), i) for i, el in enumerate(influenses)]
        heapq.heapify(influenses)
        neibs = set()
        while influenses:
            value, node = heapq.heappop(influenses)
            value = -value
            if node not in neibs:
                answer -= value // 2
                for neib in paths[node]:
                    neibs.add(neib)
        return answer


start_time = time()

# Example 1:
# Input: n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
_n = 4
_edges = [[0,1],[1,2],[1,3]]
_price = [2,2,10,6]
_trips = [[0,3],[2,1],[2,3]]
# Output: 23
# Explanation: The diagram above denotes the tree after rooting it at node 2. The first part shows the initial tree and the second part shows the tree after choosing nodes 0, 2, and 3, and making their price half.
# For the 1st trip, we choose path [0,1,3]. The price sum of that path is 1 + 2 + 3 = 6.
# For the 2nd trip, we choose path [2,1]. The price sum of that path is 2 + 5 = 7.
# For the 3rd trip, we choose path [2,1,3]. The price sum of that path is 5 + 2 + 3 = 10.
# The total price sum of all trips is 6 + 7 + 10 = 23.
# It can be proven, that 23 is the minimum answer that we can achieve.
#
# Example 2:
# Input: n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
_n = 2
_edges = [[0,1]]
_price = [2,2]
_trips = [[0,0]]
# Output: 1
# Explanation: The diagram above denotes the tree after rooting it at node 0. The first part shows the initial tree and the second part shows the tree after choosing node 0, and making its price half.
# For the 1st trip, we choose path [0]. The price sum of that path is 1.
# The total price sum of all trips is 1. It can be proven, that 1 is the minimum answer that we can achieve.

print(Solution().minimumTotalPrice(_n, _edges, _price, _trips))

print("--- %s seconds ---" % (time() - start_time))
