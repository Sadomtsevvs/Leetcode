from time import time


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        n = len(grid)

        time = 0

        def findroute():
            visited = set()
            to_visit = set()
            to_visit.add((0, 0))
            while to_visit:
                next_visit = set()
                for i, j in to_visit:
                    if grid[i][j] <= 0:
                        visited.add((i, j))
                    else:
                        continue
                    if i < n - 1:
                        if (i + 1, j) not in visited:
                            next_visit.add((i + 1, j))
                    if i > 0:
                        if (i - 1, j) not in visited:
                            next_visit.add((i - 1, j))
                    if j < n - 1:
                        if (i, j + 1) not in visited:
                            next_visit.add((i, j + 1))
                    if j > 0:
                        if (i, j - 1) not in visited:
                            next_visit.add((i, j - 1))
                if not next_visit:
                    break
                to_visit -= visited
                to_visit |= next_visit
            if (n - 1, n - 1) in visited:
                return True
            else:
                return min([grid[i][j] for i, j in to_visit])

        while True:
            res = findroute()
            if res is True:
                return time
            time += res
            for i in range(n):
                for j in range(n):
                    grid[i][j] -= res

        # heap solution from Lee, amazing
        #
        # N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        # while True:
        #     T, x, y = heapq.heappop(pq)
        #     res = max(res, T)
        #     if x == y == N - 1:
        #         return res
        #     for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        #         if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
        #             seen.add((i, j))
        #             heapq.heappush(pq, (grid[i][j], i, j))


start_time = time()

_grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

print(Solution().swimInWater(_grid))

print("--- %s seconds ---" % (time() - start_time))
