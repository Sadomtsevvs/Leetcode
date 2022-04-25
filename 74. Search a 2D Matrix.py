from time import time


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        start = 0
        end = (n - 1) + (m - 1) / m
        while end >= start:
            mid = (start + end) / 2
            i = int(mid)
            j = round((mid - i) * m)
            if j > m - 1:
                j = j - 1
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                start = i + (j + 1) / m
            else:
                end = i + (j - 1) / m
        return False


start_time = time()

_matrix = [[1, 1], [2, 2]]
3
_target = 0

print(Solution().searchMatrix(_matrix, _target))

print("--- %s seconds ---" % (time() - start_time))
