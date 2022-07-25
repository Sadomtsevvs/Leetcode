from time import time


class Solution:
    def totalNQueens(self, n: int) -> int:

        # my second solution
        #
        ans = [0]

        def count_solutions(row, cols, diag1, diag2):
            if row == n:
                ans[0] += 1
                return
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                count_solutions(row + 1, cols | {col}, diag1 | {row + col}, diag2 | {row - col})

        count_solutions(0, set(), set(), set())

        return ans[0]

        # my first solution
        #
        # result = 0
        #
        # def find(r, cols, diags1, diags2, ans):
        #     nonlocal result
        #     if r == n:
        #         result += 1
        #     for c in range(n):
        #         if c in cols or (c + r) in diags1 or (c - r) in diags2:
        #             continue
        #         find(r + 1, cols | {c}, diags1 | {(c + r)}, diags2 | {(c - r)}, ans + ['.' * c + 'Q' + '.' * (n - c - 1)])
        #
        # find(0, set(), set(), set(), [])
        # return result


start_time = time()

_n = 4
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

print(Solution().totalNQueens(_n))

print("--- %s seconds ---" % (time() - start_time))
