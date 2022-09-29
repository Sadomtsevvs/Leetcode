from time import time
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        imin, imax = -1, n
        jmin, jmax = -1, m
        i = j = 0
        result = []
        left, down, right, up = True, False, False, False
        for _ in range(n*m):
            result.append(matrix[i][j])
            if left:
                if j + 1 < jmax:
                    j += 1
                else:
                    left = False
                    imin += 1
                    down = True
                    i += 1
            elif down:
                if i + 1 < imax:
                    i += 1
                else:
                    down = False
                    jmax -= 1
                    right = True
                    j -= 1
            elif right:
                if j - 1 > jmin:
                    j -= 1
                else:
                    right = False
                    imax -= 1
                    up = True
                    i -= 1
            elif up:
                if i - 1 > imin:
                    i -= 1
                else:
                    up = False
                    jmin += 1
                    left = True
                    j += 1
        return result


start_time = time()

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

print(Solution().spiralOrder(_matrix))

print("--- %s seconds ---" % (time() - start_time))
