from time import time


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        result = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                result += 1
            else:
                end = intervals[i][1]
        return result


start_time = time()

# _intervals = [[1,2],[2,3],[3,4],[1,3]]
_intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
# Output 8
# Expected 7
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

print(Solution().eraseOverlapIntervals(_intervals))

print("--- %s seconds ---" % (time() - start_time))
