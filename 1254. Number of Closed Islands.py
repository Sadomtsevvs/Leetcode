from time import time
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        ans = 0

        def check(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            check1 = check(i - 1, j)
            check2 = check(i + 1, j)
            check3 = check(i, j - 1)
            check4 = check(i, j + 1)
            return check1 and check2 and check3 and check4

        for _i in range(len(grid)):
            for _j in range(len(grid[0])):
                if grid[_i][_j] == 0 and check(_i, _j):
                    ans += 1

        return ans


start_time = time()


# Example 1:
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
_grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation:
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
#
# Example 2:
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
_grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
#
# Output: 1
#
# Example 3:
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
_grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
# Output: 2


print(Solution().closedIsland(_grid))

print("--- %s seconds ---" % (time() - start_time))
