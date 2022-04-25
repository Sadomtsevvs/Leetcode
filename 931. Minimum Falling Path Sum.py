from time import time


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(0, len(matrix[0])):
                if j == 0 and j == len(matrix[0]) - 1:
                    matrix[i][j] += matrix[i-1][j]
                elif j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == len(matrix[0]) - 1:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        return min(matrix[-1])


start_time = time()

_matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.

print(Solution().minFallingPathSum(_matrix))

print("--- %s seconds ---" % (time() - start_time))
