from time import time


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        new_board = [row[:] for row in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                col_1 = 0
                if i > 0:
                    col_1 += int(board[i - 1][j] == 1)
                    if j > 0:
                        col_1 += int(board[i - 1][j - 1] == 1)
                    if j < len(board[0]) - 1:
                        col_1 += int(board[i - 1][j + 1] == 1)
                if i < len(board) - 1:
                    col_1 += int(board[i + 1][j] == 1)
                    if j > 0:
                        col_1 += int(board[i + 1][j - 1] == 1)
                    if j < len(board[0]) - 1:
                        col_1 += int(board[i + 1][j + 1] == 1)
                if j > 0:
                    col_1 += int(board[i][j - 1] == 1)
                if j < len(board[0]) - 1:
                    col_1 += int(board[i][j + 1] == 1)
                if new_board[i][j] == 0 and col_1 == 3:
                    new_board[i][j] = 1
                elif new_board[i][j] == 1 and (col_1 < 2 or col_1 > 3):
                    new_board[i][j] = 0
        board[:] = [row[:] for row in new_board]


start_time = time()

_board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Solution().gameOfLife(_board)
print(_board)

print("--- %s seconds ---" % (time() - start_time))
