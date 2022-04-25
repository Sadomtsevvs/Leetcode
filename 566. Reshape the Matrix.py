from time import time


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) == r and len(mat[0]) == r:
            return mat
        if len(mat) * len(mat[0]) != r * c:
            return mat
        result = []
        row = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row.append(mat[i][j])
                if len(row) == c:
                    result.append(row)
                    row = []
        return result

        # fast solution from LC comments
        #
        # rows=len(mat)
        # cols=len(mat[0])
        # if (rows*cols) != r*c:
        #     return mat
        # result=[[1 for _ in range(c)] for _ in range(r)]
        # m=0
        # n=0
        # for i in mat:
        #     for j in i:
        #         if n==c:
        #             n=0
        #             m+=1
        #         result[m][n]=j
        #         n+=1
        # return result


start_time = time()

_mat = [[1, 2], [3, 4]]
_r = 4
_c = 1
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

print(Solution().matrixReshape(_mat, _r, _c))

print("--- %s seconds ---" % (time() - start_time))
