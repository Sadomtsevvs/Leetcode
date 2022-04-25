from time import time


class Solution:
    def countRectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:

        h = [[] for _ in range(101)]
        for x, y in rectangles:
            h[y].append(x)

        for i in range(len(h)):
            h[i].sort()

        result = []

        for x, y in points:
            c = 0
            for yy in range(y, 101):
                if not h[yy] or h[yy][-1] < x:
                    continue
                if h[yy][0] >= x:
                    c += len(h[yy])
                    continue
                l, r = 0, len(h[yy])-1
                while l < r:
                    mid = (l + r) // 2
                    if h[yy][mid] >= x:
                        r = mid
                    else:
                        l = mid + 1
                c += len(h[yy]) - l

            result.append(c)

        return result

        # from LC comments
        #
        # res = []
        # n = len(rectangles)
        # dic = collections.defaultdict(list)
        # for l, h in rectangles:
        #     dic[h].append(l)
        # for h in dic:
        #     dic[h].sort()
        # # print(dic)
        # for x, y in points:
        #     count = 0
        #     for h in range(y, 101):
        #         j = bisect_left(dic[h], x)
        #         # print(h, j)
        #         count += len(dic[h]) - j
        #     res.append(count)
        # return res


start_time = time()

_rectangles = [[1,2],[2,3],[2,5]]
_points = [[2,1],[1,4]]
# _rectangles = [[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]]
# _points = [[10,3],[8,10],[2,3],[5,4],[8,5],[7,10],[6,6],[3,6]]
# Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
# Output: [2,1]
# Explanation:
# The first rectangle contains no points.
# The second rectangle contains only the point (2, 1).
# The third rectangle contains the points (2, 1) and (1, 4).
# The number of rectangles that contain the point (2, 1) is 2.
# The number of rectangles that contain the point (1, 4) is 1.
# Therefore, we return [2, 1].

print(Solution().countRectangles(_rectangles, _points))

print("--- %s seconds ---" % (time() - start_time))