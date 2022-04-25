from time import time


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        size_n = len(grid)
        size_m = len(grid[0])

        def color_island(i, j):
            if i < 0 or j < 0 or i == size_n or j == size_m:
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '2'
            color_island(i - 1, j)
            color_island(i, j - 1)
            color_island(i + 1, j)
            color_island(i, j + 1)

        result = 0
        for i in range(size_n):
            for j in range(size_m):
                if grid[i][j] != '1':
                    continue
                color_island(i, j)
                result += 1
        return result


start_time = time()

_grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(_grid))

print("--- %s seconds ---" % (time() - start_time))
