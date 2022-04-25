from time import time


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0]*n for _ in range(n)]
        i, max_i, min_i, dir_i = 0, n-1, 0,  0
        j, max_j, min_j, dir_j = 0, n-1, 0,  1
        for nn in range(1, n**2 + 1):
            result[i][j] = nn
            if j == max_j and dir_j == 1:
                min_i += 1
                dir_i = 1
                dir_j = 0
            elif i == max_i and dir_i == 1:
                dir_i = 0
                dir_j = -1
                max_j -= 1
            elif j == min_j and dir_j == -1:
                dir_i = -1
                dir_j = 0
                max_i -= 1
            elif i == min_i and dir_i == -1:
                dir_i = 0
                dir_j = 1
                min_j += 1
            i += dir_i
            j += dir_j
        return result

        # LC comments solution, great, especially matrix[y+dy][x+dx] != 0
        #
        # matrix = [[0] * n for _ in range(n)]
        # x, y, dx, dy = 0, 0, 1, 0
        # for i in range(n*n):
        #     matrix[y][x] = i + 1
        #     if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y+dy][x+dx] != 0:
        #         dx, dy = -dy, dx
        #     x, y = x + dx, y + dy
        # return matrix

start_time = time()

_n = 3
_n = 4
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

print(Solution().generateMatrix(_n))

print("--- %s seconds ---" % (time() - start_time))
