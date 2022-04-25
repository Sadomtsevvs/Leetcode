from time import time


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        result = 0
        n = len(mat)
        for i in range(n):
            result += mat[i][i] + mat[i][n-i-1]
            if i == n-i-1:
                result -= mat[i][n-i-1]
        return result


start_time = time()

_mat = [[1,2,3], [4,5,6], [7,8,9]]
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

print(Solution().diagonalSum(_mat))

print("--- %s seconds ---" % (time() - start_time))
