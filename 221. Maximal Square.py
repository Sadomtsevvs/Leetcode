from time import time


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        res = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == '1':
                    res[i][j] = 1 + min(res[i-1][j-1], res[i-1][j], res[i][j-1])
        return max([max(el) for el in res]) ** 2


start_time = time()

_matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","0","1"],["1","0","1","1","1"]]
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

print(Solution().maximalSquare(_matrix))

print("--- %s seconds ---" % (time() - start_time))
