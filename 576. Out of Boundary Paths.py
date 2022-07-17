from time import time
from collections import defaultdict


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ans = 0
        positions = defaultdict(int)
        positions[(startRow, startColumn)] = 1
        for i in range(maxMove):
            next_positions = defaultdict(int)
            for posx, posy in positions.keys():
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_positions[(posx + dx, posy + dy)] += positions[(posx, posy)]
            positions.clear()
            for x, y in next_positions.keys():
                if x < 0 or y < 0 or x == m or y == n:
                    ans += next_positions[(x, y)]
                else:
                    positions[(x, y)] = next_positions[(x, y)]
        return ans % (10**9 + 7)


start_time = time()

_m = 2
_n = 2
_maxMove = 2
_startRow = 0
_startColumn = 0
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6

# _m = 1
# _n = 3
# _maxMove = 3
# _startRow = 0
# _startColumn = 1
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12

_m = 8
_n = 50
_maxMove = 23
_startRow = 5
_startColumn = 26
# Expected: 914783380

print(Solution().findPaths(_m, _n, _maxMove, _startRow, _startColumn))

print("--- %s seconds ---" % (time() - start_time))
