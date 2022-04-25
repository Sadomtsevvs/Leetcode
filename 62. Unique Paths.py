from time import time


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[1 for _ in range(n)] for _ in range(m)]
        for j in range(1, n):
            for i in range(1, m):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[-1][-1]


start_time = time()

_m = 3
_n = 7
# Output: 28

print(Solution().uniquePaths(_m, _n))

print("--- %s seconds ---" % (time() - start_time))
