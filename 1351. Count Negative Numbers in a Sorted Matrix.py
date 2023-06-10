from time import time
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        i, j = 0, m-1
        while i < n and j >= 0:
            if grid[i][j] < 0:
                ans += (n - i)
                j -= 1
            else:
                i += 1
        return ans


start_time = time()


# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
_grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
#
# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0

print(Solution().countNegatives(_grid))

print("--- %s seconds ---" % (time() - start_time))
