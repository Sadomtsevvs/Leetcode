from time import time


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        # official solution
        dp = [[0 for _ in range(101)] for _ in range(query_row+1)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                q = (dp[i][j] - 1) / 2
                if q > 0:
                    dp[i + 1][j] += q
                    dp[i + 1][j + 1] += q
        return min(1, dp[query_row][query_glass])

        # simulation, TLE
        #
        # dp = [[0 for _ in range(100)] for _ in range(100)]
        #
        # full = 0
        #
        # for _ in range(poured):
        #     rest = 1
        #     while True:
        #         if rest == 0:
        #             break
        #         for i in range(full, 100):
        #             if rest == 0:
        #                 break
        #             for j in range(i + 1):
        #                 if dp[i][j] == 1:
        #                     continue
        #                 if i == 0:
        #                     dp[i][j] = 1
        #                     rest -= 1
        #                     full = 1
        #                     break
        #                 add = 1 / 2**i
        #                 if j == 0 and dp[i - 1][0] == 1:
        #                     dp[i][j] += add
        #                     rest -= add
        #                 elif j == i and dp[i - 1][i - 1] == 1:
        #                     dp[i][j] += add
        #                     rest -= add
        #                     if dp[i][j] == 1:
        #                         full = i + 1
        #                 else:
        #                     if dp[i - 1][j - 1] == 1:
        #                         dp[i][j] += add
        #                         rest -= add
        #                     if dp[i - 1][j] == 1:
        #                         dp[i][j] += add
        #                         rest -= add
        #
        # return dp[query_row][query_glass]


start_time = time()

# Example 1:
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)).
# There will be no excess liquid so all the glasses under the top glass will remain empty.
#
# Example 2:
# Input: poured = 2, query_row = 1, query_glass = 1
_poured = 2
_query_row = 1
_query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)).
# There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share
# the excess liquid equally, and each will get half cup of champange.
#
# Example 3:
# Input: poured = 100000009, query_row = 33, query_glass = 17
_poured = 100000009
_query_row = 33
_query_glass = 17
# Output: 1.00000

# _poured = 4
# _query_row = 2
# _query_glass = 0


print(Solution().champagneTower(_poured, _query_row, _query_glass))

print("--- %s seconds ---" % (time() - start_time))
