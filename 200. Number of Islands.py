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

        # from LC
        #
        # def sink(i, j):
        #     if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
        #         grid[i][j] = '0'
        #         map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1))
        #         return 1
        #     return 0
        #
        # return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))



start_time = time()

_grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(_grid))

print("--- %s seconds ---" % (time() - start_time))
