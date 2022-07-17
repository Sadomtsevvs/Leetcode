from time import time


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        # divide and conquer approach
        if not matrix or not matrix[0]:
            return False

        pivot_row = len(matrix) // 2
        pivot_col = len(matrix[0]) // 2
        pivot = matrix[pivot_row][pivot_col]

        if pivot == target:
            return True
        elif len(matrix) == 0 and len(matrix[0]) == 0 and matrix[0][0] != target:
            return False

        if pivot > target:
            small = [[matrix[i][j] for j in range(pivot_col)] for i in range(pivot_row, len(matrix))]
            return self.searchMatrix(small, target) or self.searchMatrix(matrix[:pivot_row], target)
        else:
            small = [[matrix[i][j] for j in range(pivot_col+1, len(matrix[0]))] for i in range(pivot_row+1)]
            return self.searchMatrix(small, target) or self.searchMatrix(matrix[pivot_row+1:], target)

        # linear time approach
        #
        # n = len(matrix) - 1
        # m = len(matrix[0]) - 1
        # i, j = 0, m
        # while i <= n and j >= 0:
        #     if matrix[i][j] == target:
        #         return True
        #     if matrix[i][j] < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return False



start_time = time()

_matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
_target = 11
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

print(Solution().searchMatrix(_matrix, _target))

print("--- %s seconds ---" % (time() - start_time))
