from time import time
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        result = []
        for j in range(len(grid[0])):
            ans = 0
            for i in range(len(grid)):
                ans = max(ans, len(str(grid[i][j])))
            result.append(ans)
        return result


start_time = time()

# Example 1:
# Input: grid = [[1],[22],[333]]
_grid = [[1],[22],[333]]
# Output: [3]
# Explanation: In the 0th column, 333 is of length 3.
#
# Example 2:
# Input: grid = [[-15,1,3],[15,7,12],[5,6,-2]]
_grid = [[-15,1,3],[15,7,12],[5,6,-2]]
# Output: [3,1,2]
# Explanation:
# In the 0th column, only -15 is of length 3.
# In the 1st column, all integers are of length 1.
# In the 2nd column, both 12 and -2 are of length 2.

print(Solution().findColumnWidth(_grid))

print("--- %s seconds ---" % (time() - start_time))
