from time import time


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()
        result = [intervals[0]]
        for beg, end in intervals:
            if beg > result[-1][1]:
                result.append([beg, end])
            elif end > result[-1][1]:
                result[-1][1] = end
        return result

        # first solution
        #
        # intervals.sort()
        # result = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= result[-1][1]:
        #         if result[-1][1] <= intervals[i][1]:
        #             result[-1][1] = intervals[i][1]
        #     else:
        #         result.append(intervals[i])
        # return result


start_time = time()

_intervals = [[1,3],[2,6],[8,10],[15,18]]
_intervals = [[1,3],[4,8],[3,5]]
_intervals = [[1,4],[1,4]]
_intervals = [[1,4],[0,4]]
_intervals = [[1,4],[2,3]]
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

print(Solution().merge(_intervals))

print("--- %s seconds ---" % (time() - start_time))
