from time import time
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # we can improve space complexity if we use intervals instead begs
        #
        ans, cur = 0, 0
        begs, ends = [], []
        for beg, end in intervals:
            begs.append(beg)
            ends.append(end)
        begs.sort()
        ends.sort()
        beg_pointer, end_pointer = 0, 0
        while beg_pointer < len(begs):
            if begs[beg_pointer] < ends[end_pointer]:
                cur += 1
                beg_pointer += 1
                ans = max(ans, cur)
            else:
                cur -= 1
                end_pointer += 1
        return ans


start_time = time()

_intervals = [[0,30],[5,10],[15,20]]
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
#
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1

print(Solution().minMeetingRooms(_intervals))

print("--- %s seconds ---" % (time() - start_time))
