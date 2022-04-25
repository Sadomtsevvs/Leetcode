from time import time


def area_of_island(_grid, i, j, size_n, size_m):
    if i < 0 or j < 0 or i == size_n or j == size_m:
        return 0
    if _grid[i][j] != 1:
        return 0
    _grid[i][j] = 2
    return 1 + area_of_island(_grid, i - 1, j, size_n, size_m) + area_of_island(_grid, i, j - 1, size_n, size_m) \
             + area_of_island(_grid, i, j + 1, size_n, size_m) + area_of_island(_grid, i + 1, j, size_n, size_m)


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue
                result = max(result, area_of_island(grid, i, j, len(grid), len(grid[0])))
        return result


start_time = time()

_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(Solution().maxAreaOfIsland(_grid))

print("--- %s seconds ---" % (time() - start_time))
