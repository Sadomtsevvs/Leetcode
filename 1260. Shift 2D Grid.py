from time import time


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                a, b = divmod(j+k, m)
                ans[(i + a) % n][b] = grid[i][j]
        return ans

        # from LC comments
        #
        # col, nums = len(grid[0]), sum(grid, [])
        # k = k % len(nums)
        # nums = nums[-k:] + nums[:-k]
        # return [nums[i:i+col] for i in range(0, len(nums), col)]


start_time = time()

_grid = [[1,2,3],[4,5,6],[7,8,9]]
_k = 1
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]

print(Solution().shiftGrid(_grid, _k))

print("--- %s seconds ---" % (time() - start_time))
