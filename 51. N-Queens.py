from time import time
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def find(r, cols, diags1, diags2, ans):
            if r == n:
                result.append(ans)
            for c in range(n):
                if c in cols or (c + r) in diags1 or (c - r) in diags2:
                    continue
                find(r + 1, cols | {c}, diags1 | {(c + r)}, diags2 | {(c - r)}, ans + ['.' * c + 'Q' + '.' * (n - c - 1)])

        find(0, set(), set(), set(), [])
        return result


start_time = time()

_n = 4
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

print(Solution().solveNQueens(_n))

print("--- %s seconds ---" % (time() - start_time))
