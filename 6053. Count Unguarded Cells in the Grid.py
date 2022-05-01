from time import time
from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid = [[0 for _ in range(n)] for _ in range(m)]

        for i, j in guards:
            grid[i][j] = 1
        for i, j in walls:
            grid[i][j] = 2

        for i in range(m):
            danger = False
            for j in range(n):
                if grid[i][j] == 2:
                    danger = False
                elif grid[i][j] == 1:
                    danger = True
                elif danger:
                    grid[i][j] = 3
            danger = False
            for j in range(n-1, -1, -1):
                if grid[i][j] == 2:
                    danger = False
                elif grid[i][j] == 1:
                    danger = True
                elif danger:
                    grid[i][j] = 3

        for j in range(n):
            danger = False
            for i in range(m):
                if grid[i][j] == 2:
                    danger = False
                elif grid[i][j] == 1:
                    danger = True
                elif danger:
                    grid[i][j] = 3
            danger = False
            for i in range(m-1, -1, -1):
                if grid[i][j] == 2:
                    danger = False
                elif grid[i][j] == 1:
                    danger = True
                elif danger:
                    grid[i][j] = 3

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1

        return ans



start_time = time()

# _m = 4
# _n = 6
# _guards = [[0,0],[1,1],[2,3]]
# _walls = [[0,1],[2,2],[1,4]]
_m = 2
_n = 7
_guards = [[1,5],[1,1],[1,6],[0,2]]
_walls = [[0,6],[0,3],[0,5]]
# _m = 3
# _n = 3
# _guards = [[1,1]]
# _walls = [[0,1],[1,0],[2,1],[1,2]]
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.

print(Solution().countUnguarded(_m, _n, _guards, _walls))

print("--- %s seconds ---" % (time() - start_time))
