from time import time
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        return res

        # official solution
        #
        # R, C = len(A), len(A[0])
        # ans = [[None] * R for _ in xrange(C)]
        # for r, row in enumerate(A):
        #     for c, val in enumerate(row):
        #         ans[c][r] = val
        # return ans

        #Alternative Solution:
        #return zip(*A)

        # from LC comments
        #
        # return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


start_time = time()

_matrix = [[1,2,3],[4,5,6]]
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

print(Solution().transpose(_matrix))

print("--- %s seconds ---" % (time() - start_time))
