from time import time
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        subs = [set() for i in range(9)] # subs: 0 1 2
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    subs[3*(i//3) + j//3].add(int(board[i][j]))

        def solve(i, j, rows, cols, subs):
            if j == 9:
                i += 1
                j = 0
            if i == 9:
                return True
            if board[i][j] != '.':
                return solve(i, j+1, rows, cols, subs)
            for num in range(1, 10):
                if num in rows[i] or num in cols[j] or num in subs[3*(i//3) + j//3]:
                    continue
                board[i][j] = str(num)
                rows[i].add(num)
                cols[j].add(num)
                subs[3*(i//3) + j//3].add(num)
                if solve(i, j+1, rows, cols, subs):
                    return True
                board[i][j] = '.'
                rows[i].remove(num)
                cols[j].remove(num)
                subs[3*(i//3) + j//3].remove(num)
            return False

        solve(0, 0, rows, cols, subs)


start_time = time()

_board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
#                 [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
#                 ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
#                 [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
#                 [".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],
#          ["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],
#          ["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
#          ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],
#          ["3","4","5","2","8","6","1","7","9"]]

Solution().solveSudoku(_board)
print(_board)

print("--- %s seconds ---" % (time() - start_time))
