from time import time
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        result = []
        up_right = True
        i, j = 1, -1
        while i != n - 1 or j != m - 1:
            if up_right:
                if j == m - 1:
                    i += 1
                    up_right = not up_right
                elif i == 0:
                    j += 1
                    up_right = not up_right
                else:
                    i -= 1
                    j += 1
            else:
                if i == n - 1:
                    j += 1
                    up_right = not up_right
                elif j == 0:
                    i += 1
                    up_right = not up_right
                else:
                    i += 1
                    j -= 1
            result.append(mat[i][j])
        return result

        # from LC
        #
        # d = collections.defaultdict(list)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         d[i + j].append(matrix[i][j])
        # out = []
        # for k, v in d.items():
        #     if k % 2 == 0:
        #         out += v[::-1]
        #     else:
        #         out += v
        # return out


start_time = time()

_mat = [[1,2,3],[4,5,6],[7,8,9]]
# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
#
# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

print(Solution().findDiagonalOrder(_mat))

print("--- %s seconds ---" % (time() - start_time))
