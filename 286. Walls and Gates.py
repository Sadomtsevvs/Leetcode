from time import time
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        wall, gate, empty = -1, 0, 2147483647

        n, m = len(rooms), len(rooms[0])

        next_moves = set()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        if i+x < 0 or j+y < 0 or i+x == n or j+y == m:
                            continue
                        if rooms[i+x][j+y] != empty:
                            continue
                        next_moves.add((i + x, j + y))

        def dfs(moves, dist):
            if not moves:
                return
            next_moves = set()
            for i, j in moves:
                if rooms[i][j] != empty:
                    continue
                rooms[i][j] = dist
                for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    if i + x < 0 or j + y < 0 or i + x == n or j + y == m:
                        continue
                    if rooms[i+x][j+y] != empty:
                        continue
                    next_moves.add((i + x, j + y))
            dfs(list(next_moves), dist + 1)

        dfs(list(next_moves), 1)


start_time = time()

_rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Example 1:
# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
#
# Example 2:
# Input: rooms = [[-1]]
# Output: [[-1]]

print(Solution().wallsAndGates(_rooms))

print("--- %s seconds ---" % (time() - start_time))
