from time import time
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        nimg = [[img[i][j] for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(1, m):
                nimg[i][j] += img[i][j-1]
            for j in range(m-2, -1, -1):
                nimg[i][j] += img[i][j+1]
        nimg2 = [[nimg[i][j] for j in range(m)] for i in range(n)]
        for j in range(m):
            for i in range(1, n):
                nimg2[i][j] += nimg[i-1][j]
            for i in range(n-2, -1, -1):
                nimg2[i][j] += nimg[i+1][j]
        for i in range(n):
            for j in range(m):
                if (i == 0 and (j == 0 or j == m-1)) or (i == n-1 and (j == 0 or j == m-1)):
                    if n == 1 and m == 1:
                        d = 1
                    elif m == 1 or n == 1:
                        d = 2
                    else:
                        d = 4
                elif i == 0 or i == n-1 or j == 0 or j == m-1:
                    if n == 1 or m == 1:
                        d = 3
                    else:
                        d = 6
                else:
                    d = 9
                nimg2[i][j] //= d
        return nimg2

        # # official solution
        # #
        # # Save the dimensions of the image.
        # m = len(img)
        # n = len(img[0])
        #
        # # Create a new image of the same dimension as the input image.
        # smooth_img = [[0] * n for _ in range(m)]
        #
        # # Iterate over the cells of the image.
        # for i in range(m):
        #     for j in range(n):
        #         # Initialize the sum and count
        #         sum = 0
        #         count = 0
        #
        #         # Iterate over all plausible nine indices.
        #         for x in (i - 1, i, i + 1):
        #             for y in (j - 1, j, j + 1):
        #                 # If the indices form valid neighbor
        #                 if 0 <= x < m and 0 <= y < n:
        #                     sum += img[x][y]
        #                     count += 1
        #
        #         # Store the rounded down value in smooth_img[i][j].
        #         smooth_img[i][j] = sum // count
        #
        # # Return the smooth image.
        # return smooth_img

start_time = time()

# Example 1:
# Input: img = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[0,0,0],[0,0,0],[0,0,0]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
#
# Example 2:
# Input: img = [[100,200,100],[200,50,200],[100,200,100]]
_img = [[100,200,100],[200,50,200],[100,200,100]]
# Output: [[137,141,137],[141,138,141],[137,141,137]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
# For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
# For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

print(Solution().imageSmoother(_img))

print("--- %s seconds ---" % (time() - start_time))
