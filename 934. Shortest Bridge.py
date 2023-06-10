from time import time
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)
        first, second = set(), set()

        def mark_island(island, i, j):
            if i < 0 or j < 0 or i >= n or j >= n:
                return
            if grid[i][j] == 0:
                return
            island.add((i, j))
            grid[i][j] = 0
            mark_island(island, i + 1, j)
            mark_island(island, i - 1, j)
            mark_island(island, i, j + 1)
            mark_island(island, i, j - 1)

        one = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if one:
                        one = False
                        mark_island(first, i, j)
                    else:
                        mark_island(second, i, j)
                        break
            if second:
                break
        ans = 0
        check = first
        while True:
            add_land = set()
            for i, j in check:
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                    if ni < 0 or nj < 0 or ni >= n or nj >= n:
                        continue
                    if (ni, nj) in second:
                        return ans
                    if (ni, nj) in first:
                        continue
                    add_land.add((ni, nj))
            first.update(add_land)
            check = add_land
            ans += 1
        return -1


start_time = time()

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 1
_grid = [[0,1],[1,0]]
#
# Example 2:
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# _grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
#
# Example 3:
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# _grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1

# _grid = [[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]

print(Solution().shortestBridge(_grid))

print("--- %s seconds ---" % (time() - start_time))
