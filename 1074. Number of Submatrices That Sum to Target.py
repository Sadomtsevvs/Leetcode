from time import time
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:


start_time = time()


# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.

_matrix = [[1,-1],[-1,1]]
_target = 0
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

print(Solution().numSubmatrixSumTarget(_matrix, _target))

print("--- %s seconds ---" % (time() - start_time))
