from time import time


class Solution:
    def exist(self, board:list[list[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])

        def bt(remain, i, j, seen):
            if not remain:
                return True
            if i > 0 and board[i - 1][j] == remain[0] and (i - 1, j) not in seen:
                if bt(remain[1:], i - 1, j, seen | {(i - 1, j)}):
                    return True
            if j > 0 and board[i][j - 1] == remain[0] and (i, j - 1) not in seen:
                if bt(remain[1:], i, j - 1, seen | {(i, j - 1)}):
                    return True
            if i < n - 1 and board[i + 1][j] == remain[0] and (i + 1, j) not in seen:
                if bt(remain[1:], i + 1, j, seen | {(i + 1, j)}):
                    return True
            if j < m - 1 and board[i][j + 1] == remain[0] and (i, j + 1) not in seen:
                if bt(remain[1:], i, j + 1, seen | {(i, j + 1)}):
                    return True
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if bt(word[1:], i, j, {(i, j)}):
                        return True

        return False


start_time = time()

# _board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# _word = "ABCCED"
_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
_word = "ABCB"

# Output: true

print(Solution().exist(_board, _word))

print("--- %s seconds ---" % (time() - start_time))
