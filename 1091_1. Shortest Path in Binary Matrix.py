from time import time
from typing import List


class Node:
    def __init__(self, i, j, parent):
        self.i = i
        self.j = j
        self.parent = parent

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> list[tuple[int, int]]:

        # solution with find the path, not length
        if grid[0][0] == 1:
            return []

        n, m = len(grid), len(grid[0])
        start_node = Node(0,0,None)
        queue = [start_node]
        for node in queue:
            i, j = node.i, node.j
            for x, y in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                         (i + 1, j + 1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    next_node = Node(x, y, node)
                    queue.append(next_node)
                    if x == n-1 and y == m-1:
                        path = []
                        nd = next_node
                        while nd:
                            path.append((nd.i, nd.j))
                            nd = nd.parent
                        return path[::-1]
        return []



        # # i have done it with dynamic programming, but it is not efficient
        #
        # n = len(grid)
        #
        # if not grid or grid[0][0] != 0 or grid[n-1][n-1] != 0:
        #     return -1
        #
        # nulls_to_continue = [(0, 0)]
        # result = [[float('inf') for _ in range(n)] for _ in range(n)]
        # result[0][0] = 1
        #
        # def neighbours0(i, j):
        #     neighbours_all = []
        #     if i > 0:
        #         neighbours_all.append((i - 1, j))
        #         if j > 0:
        #             neighbours_all.append((i - 1, j - 1))
        #         if j < n - 1:
        #             neighbours_all.append((i - 1, j + 1))
        #     if i < n - 1:
        #         neighbours_all.append((i + 1, j))
        #         if j > 0:
        #             neighbours_all.append((i + 1, j - 1))
        #         if j < n - 1:
        #             neighbours_all.append((i + 1, j + 1))
        #     if j > 0:
        #         neighbours_all.append((i, j - 1))
        #     if j < n - 1:
        #         neighbours_all.append((i, j + 1))
        #     neighbours0 = [(nei[0], nei[1]) for nei in neighbours_all if grid[nei[0]][nei[1]] == 0]
        #     return neighbours0
        #
        # while nulls_to_continue:
        #     another_nulls_to_continue = []
        #     while nulls_to_continue:
        #         null = nulls_to_continue.pop()
        #         i, j = null[0], null[1]
        #         for nei in neighbours0(i, j):
        #             if result[nei[0]][nei[1]] < float('inf'):
        #                 continue
        #             result[nei[0]][nei[1]] = 1 + min([result[ii][jj] for ii, jj in neighbours0(nei[0], nei[1])])
        #             another_nulls_to_continue.append((nei[0], nei[1]))
        #     nulls_to_continue = another_nulls_to_continue
        #
        # return result[n-1][n-1] if result[n-1][n-1] < float('inf') else -1

        # good solution from comments
        #
        # n = len(grid)

        # if grid[0][0] or grid[n - 1][n - 1]:
            # return -1

        # queue = [(0, 0, 1)]
        # grid[0][0] = 1

        # for i, j, depth in queue:
            # if i == n - 1 and j == n - 1:
                # return depth
            # for x, y in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                         # (i + 1, j + 1)):
                # if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    # grid[x][y] = 1
                    # queue.append((x, y, depth + 1))
        # return -1


start_time = time()

_grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
# _grid = [[0,0,0],[0,1,0],[0,0,0]]
# _grid = [[0,0,0,0],[1,0,0,1],[0,1,0,0],[0,0,0,0]]
# _grid = [[0,1,0,0,0,0],[0,1,1,1,1,1],[0,0,0,0,1,1],[0,1,0,0,0,1],[1,0,0,1,0,1],[0,0,1,0,1,0]]
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

print(Solution().shortestPathBinaryMatrix(_grid))

print("--- %s seconds ---" % (time() - start_time))
