from time import time


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


start_time = time()

_grid = [[1,3,1],[1,5,1],[4,2,1]]
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

print(Solution().minPathSum(_grid))

print("--- %s seconds ---" % (time() - start_time))
