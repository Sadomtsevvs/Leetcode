import heapq
from collections import defaultdict
from time import time
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        result = []
        cur = defaultdict(int)
        heights = []
        heapq.heapify(heights)
        buildings.sort(key=lambda x: (x[0], -x[2]))
        ends = sorted(buildings, key=lambda x: (x[1], x[2]))
        # two pointers
        p_beg, p_end = 0, 0
        while p_end < len(buildings):
            # check for the last
            if p_beg < len(buildings):
                beg = buildings[p_beg]
            else:
                beg = [float('inf')]
            end = ends[p_end]
            if beg[0] <= end[1]:
                p_beg += 1
                height = beg[2]
                cur[height] += 1
                if cur[height] > 1:
                    continue
                if not heights or -heights[0] < height:
                    result.append([beg[0], height])
                heapq.heappush(heights, -height)
            else:
                p_end += 1
                height = end[2]
                cur[height] -= 1
                if cur[height] > 0:
                    continue
                if -heights[0] == height:
                    heapq.heappop(heights)
                    while heights and cur[-heights[0]] == 0:
                        heapq.heappop(heights)
                    result.append([end[1], 0 if not heights else -heights[0]])
        return result

        # from LC
        #
        # # for the same x, (x, -H) should be in front of (x, 0)
        # # For Example 2, we should process (2, -3) then (2, 0), as there's no height change
        # x_height_right_tuples = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, "doesn't matter") for _, R, _ in buildings])
        # # (0, float('inf')) is always in max_heap, so max_heap[0] is always valid
        # result, max_heap = [[0, 0]], [(0, float('inf'))]
        # for x, negative_height, R in x_height_right_tuples:
        #     while x >= max_heap[0][1]:
        #         # reduce max height up to date, i.e. only consider max height in the right side of line x
        #         heapq.heappop(max_heap)
        #     if negative_height:
        #         # Consider each height, as it may be the potential max height
        #         heapq.heappush(max_heap, (negative_height, R))
        #     curr_max_height = -max_heap[0][0]
        #     if result[-1][1] != curr_max_height:
        #         result.append([x, curr_max_height])
        # return result[1:]


start_time = time()

_buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Example 1:
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
#
# Example 2:
# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]

print(Solution().getSkyline(_buildings))

print("--- %s seconds ---" % (time() - start_time))
