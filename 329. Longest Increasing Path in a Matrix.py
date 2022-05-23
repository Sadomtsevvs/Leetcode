from time import time
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])
        result = [[0 for _ in range(m)] for _ in range(n)]

        def count_path(ii, jj):
            res = 1
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= ii + x < n and 0 <= jj + y < m and matrix[ii][jj] < matrix[ii + x][jj + y]:
                    if result[ii + x][jj + y] == 0:
                        count_path(ii + x, jj + y)
                    res = max(res, 1 + result[ii + x][jj + y])
            result[ii][jj] = res

        for i in range(n):
            for j in range(m):
                if result[i][j] == 0:
                    count_path(i, j)

        return max(max(j for j in row) for row in result)


start_time = time()

_matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# _matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

print(Solution().longestIncreasingPath(_matrix))

print("--- %s seconds ---" % (time() - start_time))
