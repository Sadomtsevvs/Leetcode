from time import time
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        result = 0

        set_img1 = set()
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    set_img1.add((i, j))

        set_img2 = set()
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    set_img2.add((i, j))

        for shift_x in range(-n + 1, n):
            for shift_y in range(0, -n, -1):
                cur = 0
                ones = 0
                for x, y in set_img1:
                    new_x = x + shift_x
                    new_y = y + shift_y
                    if 0 <= new_x < n and 0 <= new_y < n:
                        ones += 1
                        if (new_x, new_y) in set_img2:
                            cur += 1
                if ones == 0:
                    break
                result = max(result, cur)
            for shift_y in range(1, n):
                cur = 0
                ones = 0
                for x, y in set_img1:
                    new_x = x + shift_x
                    new_y = y + shift_y
                    if 0 <= new_x < n and 0 <= new_y < n:
                        ones += 1
                        if (new_x, new_y) in set_img2:
                            cur += 1
                if ones == 0:
                    break
                result = max(result, cur)

        return result


start_time = time()

_img1 = [[1,1,0],[0,1,0],[0,1,0]]
_img2 = [[0,0,0],[0,1,1],[0,0,1]]
# Example 1:
# Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# Output: 3
# Explanation: We translate img1 to right by 1 unit and down by 1 unit.
# The number of positions that have a 1 in both images is 3 (shown in red).
#
# Example 2:
# Input: img1 = [[1]], img2 = [[1]]
# Output: 1
#
# Example 3:
# Input: img1 = [[0]], img2 = [[0]]
# Output: 0

print(Solution().largestOverlap(_img1, _img2))

print("--- %s seconds ---" % (time() - start_time))
