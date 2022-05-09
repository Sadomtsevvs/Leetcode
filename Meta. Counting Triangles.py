from time import time


class Solution:
    def countDistinctTriangles(self, arr):
        sets = set()
        for a in arr:
            sets.add(tuple(sorted(a)))
        return len(sets)


start_time = time()

_arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
_arr = [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
# arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
# output = 2
# The first two triangles are the same, so there are only 2 distinct triangles.

print(Solution().countDistinctTriangles(_arr))

print("--- %s seconds ---" % (time() - start_time))
