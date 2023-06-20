from collections import defaultdict
from time import time
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows = defaultdict(int)
        for i in range(len(grid)):
            # row = []
            # for j in range(len(grid)):
            #     row.append(grid[i][j])
            # rows[tuple(row)] += 1
            rows[tuple(grid[i])] += 1

        cols = defaultdict(int)
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cols[tuple(col)] += 1

        ans = 0

        for row, num in rows.items():
            ans += num * cols[row]

        return ans


start_time = time()

# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
#
# Example 2:
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
_grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

print(Solution().equalPairs(_grid))

print("--- %s seconds ---" % (time() - start_time))
