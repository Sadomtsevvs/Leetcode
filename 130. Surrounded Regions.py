from time import time


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def mark_region(i, j):
            if board[i][j] != "O":
                return
            board[i][j] = "OO"
            if i > 0:
                mark_region(i - 1, j)
            if i < n - 1:
                mark_region(i + 1, j)
            if j > 0:
                mark_region(i, j - 1)
            if j < m - 1:
                mark_region(i, j + 1)

        for i in {0, n - 1}:
            for j in range(m):
                mark_region(i, j)
        for j in {0, m - 1}:
            for i in range(n):
                mark_region(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "OO":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


start_time = time()

_board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Solution().solve(_board)

print(_board)

print("--- %s seconds ---" % (time() - start_time))
