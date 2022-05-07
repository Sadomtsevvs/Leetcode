from time import time


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1]\
                    = matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]

    # official transpose & reflect solution
    #
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     self.transpose(matrix)
    #     self.reflect(matrix)
    #
    # def transpose(self, matrix):
    #     n = len(matrix)
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    #
    # def reflect(self, matrix):
    #     n = len(matrix)
    #     for i in range(n):
    #         for j in range(n // 2):
    #             matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]



start_time = time()

_matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
_matrix = [[5,1,9],[2,4,8],[13,3,6]]
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Solution().rotate(_matrix)
print(_matrix)

print("--- %s seconds ---" % (time() - start_time))
