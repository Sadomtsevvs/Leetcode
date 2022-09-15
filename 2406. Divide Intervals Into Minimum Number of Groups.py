import heapq
from time import time
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heapq.heapify(heap)
        for beg, end in intervals:
            if not heap:
                heapq.heappush(heap, end)
            elif heap[0] < beg:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)


start_time = time()

_intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# Example 1:
# Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# Output: 3
# Explanation: We can divide the intervals into the following groups:
# - Group 1: [1, 5], [6, 8].
# - Group 2: [2, 3], [5, 10].
# - Group 3: [1, 10].
# It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
#
# Example 2:
# Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
# Output: 1
# Explanation: None of the intervals overlap, so we can put all of them in one group.

_s = "hdklqkcssgxlvehva" # hdklq + kcs + sgxlveh + va
# Output: 2
# Expected: 4

print(Solution().minGroups(_intervals))

print("--- %s seconds ---" % (time() - start_time))
