from time import time


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # n = len(mat)
        # m = len(mat[0])
        # result = [i[:] for i in mat]
        # next_i_j = set()
        # for i in range(n):
        #     for j in range(m):
        #         if result[i][j] != 0:
        #             result[i][j] = 20000
        #         else:
        #             if i > 0 and result[i-1][j] != 0:
        #                 next_i_j.add((i-1, j))
        #             if j > 0 and result[i][j-1] != 0:
        #                 next_i_j.add((i, j-1))
        #             if i < n - 1 and result[i+1][j] != 0:
        #                 next_i_j.add((i+1, j))
        #             if j < m - 1 and result[i][j+1] != 0:
        #                 next_i_j.add((i, j+1))
        # next = 1
        # while next_i_j:
        #     next_next_i_j = set()
        #     for i, j in next_i_j:
        #         result[i][j] = next
        #     for i, j in next_i_j:
        #         if i > 0 and result[i - 1][j] == 20000:
        #             next_next_i_j.add((i - 1, j))
        #         if j > 0 and result[i][j - 1] == 20000:
        #             next_next_i_j.add((i, j - 1))
        #         if i < n - 1 and result[i + 1][j] == 20000:
        #             next_next_i_j.add((i + 1, j))
        #         if j < m - 1 and result[i][j + 1] == 20000:
        #             next_next_i_j.add((i, j + 1))
        #     next_i_j = next_next_i_j.copy()
        #     next += 1
        # return result

        result = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        seen = set()
        next_cells = set()
        for i in range(len(mat)):
            row = mat[i]
            for j in range(len(mat[0])):
                if row[j] == 0:
                    next_cells.add((i, j))
        dist = 0
        while next_cells:
            n_next_cells = set()
            for i, j in next_cells:
                seen.add((i, j))
                result[i][j] = dist
                for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    next_i, next_j = i + x, j + y
                    if next_i < 0 or next_i > len(mat) - 1 or next_j < 0 or next_j > len(mat[0]) - 1:
                        continue
                    if (next_i, next_j) in seen:
                        continue
                    if (next_i, next_j) in next_cells:
                        continue
                    n_next_cells.add((next_i, next_j))
            next_cells = n_next_cells.copy()
            dist += 1

        return result

''' not my solution, but great

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] != 0:
                    up = math.inf if row == 0 else mat[row-1][col]
                    left = math.inf if col == 0 else mat[row][col-1]
                    mat[row][col] = min(up,left) + 1
        
        for row in range(len(mat)-1, -1, -1):
            for col in range(len(mat[0])-1, -1, -1):
                if mat[row][col] != 0:
                    down = math.inf if row == len(mat)-1 else mat[row+1][col]
                    right = math.inf if col == len(mat[0])-1 else mat[row][col+1]
                    mat[row][col] = min(mat[row][col], down+1, right+1)
        
        return mat
        
'''

start_time = time()

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
_mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

print(Solution().updateMatrix(_mat))

print("--- %s seconds ---" % (time() - start_time))
