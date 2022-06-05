from time import time
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        def find(r, cols, diags1, diags2, ans):
            nonlocal result
            if r == n:
                result += 1
            for c in range(n):
                if c in cols or (c + r) in diags1 or (c - r) in diags2:
                    continue
                find(r + 1, cols | {c}, diags1 | {(c + r)}, diags2 | {(c - r)}, ans + ['.' * c + 'Q' + '.' * (n - c - 1)])

        find(0, set(), set(), set(), [])
        return result


start_time = time()

_n = 4
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

print(Solution().totalNQueens(_n))

print("--- %s seconds ---" % (time() - start_time))
