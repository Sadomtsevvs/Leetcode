from time import time


class Solution:
    def countLatticePoints(self, circles: list[list[int]]) -> int:
        result = set()
        for x_c, y_c, r_c in circles:
            for x in range(x_c - r_c, x_c + r_c + 1):
                for y in range(y_c - r_c, y_c + r_c + 1):
                    if (x,y) not in result:
                        if (x - x_c) ** 2 + (y - y_c) ** 2 <= r_c ** 2:
                            result |= {(x,y)}
        return len(result)


start_time = time()

_circles = [[2,2,2],[3,4,1]]
# Input: circles = [[2,2,2],[3,4,1]]
# Output: 16
# Explanation:
# The figure above shows the given circles.
# There are exactly 16 lattice points which are present inside at least one circle.
# Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).

print(Solution().countLatticePoints(_circles))

print("--- %s seconds ---" % (time() - start_time))