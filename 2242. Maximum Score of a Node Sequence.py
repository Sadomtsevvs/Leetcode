from time import time
from heapq import *


class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:

        # idea from Lee

        neighbs = [[] for _ in range(len(scores))]
        for i, j in edges:
            neighbs[i].append([scores[j], j])
            neighbs[j].append([scores[i], i])
        for i in range(len(scores)):
            neighbs[i] = nlargest(3, neighbs[i])
        ans = -1
        for i, j in edges:
            for score_ii, ii in neighbs[i]:
                if ii == j:
                    continue
                for score_jj, jj in neighbs[j]:
                    if jj == i or jj == ii:
                        continue
                    ans = max(ans, score_ii + scores[i] + scores[j] + score_jj)
        return ans


start_time = time()

_scores = [5,2,9,8,4]
_edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
# Input: scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
# Output: 24
# Explanation: The figure above shows the graph and the chosen node sequence [0,1,2,3].
# The score of the node sequence is 5 + 2 + 9 + 8 = 24.
# It can be shown that no other node sequence has a score of more than 24.
# Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.
# The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.

print(Solution().maximumScore(_scores, _edges))

print("--- %s seconds ---" % (time() - start_time))
