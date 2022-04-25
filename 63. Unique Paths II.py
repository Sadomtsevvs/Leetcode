from time import time


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        result = [[0] * (len(obstacleGrid[0]) + 1)] + [[0] + row[:] for row in obstacleGrid]
        result[1][1] = 1
        for i in range(1, len(obstacleGrid) + 1):
            for j in range(1, len(obstacleGrid[0]) + 1):
                if i == 1 and j == 1:
                    pass
                elif result[i][j] == 1:
                    result[i][j] = 0
                else:
                    result[i][j] = result[i-1][j] + result[i][j-1]
        return result[-1][-1]


start_time = time()

_obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
_obstacleGrid = [[0,1],[0,0]]
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

print(Solution().uniquePathsWithObstacles(_obstacleGrid))

print("--- %s seconds ---" % (time() - start_time))
