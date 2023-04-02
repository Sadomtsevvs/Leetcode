from collections import defaultdict
from time import time
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        paths = defaultdict(list)
        for a, b, dist in roads:
            paths[a].append((b, dist))
            paths[b].append((a, dist))
        result = float('inf')
        seen = set()
        nodes = {1}
        while nodes:
            node = nodes.pop()
            for next_node, dist in paths[node]:
                if next_node in seen:
                    continue
                nodes.add(next_node)
                result = min(result, dist)
            seen.add(node)
        return result


start_time = time()

# Example 1:
# Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Output: 5
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
# It can be shown that no other path has less score.
#
_n = 4
_roads = [[1,2,2],[1,3,4],[3,4,7]]
# Example 2:
# Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
# Output: 2
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

print(Solution().minScore(_n, _roads))

print("--- %s seconds ---" % (time() - start_time))
