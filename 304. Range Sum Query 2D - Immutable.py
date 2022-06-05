from time import time
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.matrix[i][j] += matrix[i][j-1]

        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                self.matrix[i][j] += matrix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2]
        if row1 > 0:
            ans -= self.matrix[row1-1][col2]
        if col1 > 0:
            ans -= self.matrix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            ans += self.matrix[row1-1][col1 - 1]
        return ans

    # first solution
    #
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix
    #     for i in range(len(matrix)):
    #         for j in range(1, len(matrix[0])):
    #             self.matrix[i][j] += matrix[i][j-1]
    #
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     ans = 0
    #     for i in range(row1, row2 + 1):
    #         ans += self.matrix[i][col2]
    #         if col1 > 0:
    #             ans -= self.matrix[i][col1 - 1]
    #     return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

start_time = time()
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
#
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
#
# print(Solution().transpose(_matrix))

print("--- %s seconds ---" % (time() - start_time))
