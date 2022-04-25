from time import time


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh_present = False
        next_i_j = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_present = True
                    continue
                if grid[i][j] == 0:
                    continue
                if i > 0 and grid[i-1][j] == 1:
                    next_i_j.add((i-1, j))
                if j > 0 and grid[i][j-1] == 1:
                    next_i_j.add((i, j-1))
                if i < n - 1 and grid[i+1][j] == 1:
                    next_i_j.add((i+1, j))
                if j < m - 1 and grid[i][j+1] == 1:
                    next_i_j.add((i, j+1))
        if not fresh_present:
            return 0
        minutes = 0
        while next_i_j:
            next_next_i_j = set()
            for i, j in next_i_j:
                grid[i][j] = 2
            for i, j in next_i_j:
                if i > 0 and grid[i-1][j] == 1:
                    next_next_i_j.add((i-1, j))
                if j > 0 and grid[i][j-1] == 1:
                    next_next_i_j.add((i, j-1))
                if i < n - 1 and grid[i+1][j] == 1:
                    next_next_i_j.add((i+1, j))
                if j < m - 1 and grid[i][j+1] == 1:
                    next_next_i_j.add((i, j+1))
            next_i_j = next_next_i_j.copy()
            minutes += 1
        # check if fresh oranges still exist
        if len([True for i in grid for j in i if j == 1]) > 0:
            return -1
        return minutes

        # pretty bfs solution from LC comments
        #
        # m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        # for i, j in product(range(m), range(n)):
        #     if grid[i][j] == 2: queue.append((i, j))
        #     if grid[i][j] == 1: fresh += 1
        # dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # levels = 0
        #
        # while queue:
        #     levels += 1
        #     for _ in range(len(queue)):
        #         x, y = queue.popleft()
        #         for dx, dy in dirs:
        #             if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == 1:
        #                 fresh -= 1
        #                 grid[x + dx][y + dy] = 2
        #                 queue.append((x + dx, y + dy))
        #
        # return -1 if fresh != 0 else max(levels - 1, 0)


start_time = time()

# _grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
_grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]

print(Solution().orangesRotting(_grid))

print("--- %s seconds ---" % (time() - start_time))
