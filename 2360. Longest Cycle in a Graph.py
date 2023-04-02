from time import time
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        to_visit = set(range(len(edges)))
        while to_visit:
            node = to_visit.pop()
            seen = {node: 1}
            while edges[node] not in seen and edges[node] in to_visit:
                node = edges[node]
                seen[node] = len(seen) + 1
                to_visit.discard(node)
            if edges[node] in seen:
                ans = max(ans, len(seen) - seen[edges[node]] + 1)
        return ans


start_time = time()

# Example 1:
# Input: edges = [3,3,4,2,3]
# Output: 3
# Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
# The length of this cycle is 3, so 3 is returned.
_edges = [3,3,4,2,3]
#
# Example 2:
# Input: edges = [2,-1,3,1]
# Output: -1
# Explanation: There are no cycles in this graph.
# _edges = [2,-1,3,1]

edges = [3,4,0,2,-1,2]
# Output 2
# Expected 3


print(Solution().longestCycle(_edges))

print("--- %s seconds ---" % (time() - start_time))
