from time import time
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        ans = 0

        def check(i, j):
            nonlocal size
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] == 0:
                return True
            grid[i][j] = 0
            size += 1
            check1 = check(i - 1, j)
            check2 = check(i + 1, j)
            check3 = check(i, j - 1)
            check4 = check(i, j + 1)
            return check1 and check2 and check3 and check4

        for _i in range(len(grid)):
            for _j in range(len(grid[0])):
                size = 0
                if grid[_i][_j] == 1 and check(_i, _j):
                    ans += size

        return ans


start_time = time()


# Example 1:
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
_grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
#
# Example 2:
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.


print(Solution().numEnclaves(_grid))

print("--- %s seconds ---" % (time() - start_time))
