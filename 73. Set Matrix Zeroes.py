from time import time


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows0, cols0 = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows0.add(i)
                    cols0.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows0 or j in cols0:
                    matrix[i][j] = 0


start_time = time()

_matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

print(Solution().setZeroes(_matrix))

print("--- %s seconds ---" % (time() - start_time))
