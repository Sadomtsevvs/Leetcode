from time import time


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            nums = set()
            for col in row:
                if col == '.':
                    continue
                if col in nums:
                    return False
                nums.add(col)
        for col in range(9):
            nums = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in nums:
                    return False
                nums.add(board[row][col])
        for square in range(9):
            nums = set()
            for row in range(square//3 * 3, (square//3 + 1) * 3):
                for col in range(square%3 * 3, (square%3 + 1) * 3):
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in nums:
                        return False
                    nums.add(board[row][col])
        return True


start_time = time()

_board = [[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]]

# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

print(Solution().isValidSudoku(_board))

print("--- %s seconds ---" % (time() - start_time))
