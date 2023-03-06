from typing import List
from time import time


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def grid_value(_grid, _i, _j, _n):
    value = _grid[_i][_j]
    for i in range(_i, _i+_n):
        for j in range(_j, _j+_n):
            if _grid[i][j] != value:
                return 2
    return value


class Solution:
    def construct(self, grid: List[List[int]], i=0, j=0, n=0) -> 'Node':
        if n == 0:
            n = len(grid)
        val = grid_value(grid, i, j, n)
        if val == 2:
            top_left = self.construct(grid, i, j, n // 2)
            top_right = self.construct(grid, i, j + n // 2, n // 2)
            bottom_left = self.construct(grid, i + n // 2, j, n // 2)
            bottom_right = self.construct(grid, i + n // 2, j + n // 2, n // 2)
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)
        else:
            return Node(val, True, None, None, None, None)


start_time = time()

_grid = [[1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0]]

print(Solution().construct(_grid))

print("--- %s seconds ---" % (time() - start_time))