from time import time
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        diag_ids = dict()
        for i in range(n):
            for j in range(m):
                num = matrix[i][j]
                diag_id = i - j
                if diag_id not in diag_ids:
                    diag_ids[diag_id] = num
                elif diag_ids[diag_id] != num:
                    return False
        return True


start_time = time()

_matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
#
# Example 2:
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.

print(Solution().isToeplitzMatrix(_matrix))

print("--- %s seconds ---" % (time() - start_time))
