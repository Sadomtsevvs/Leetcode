from time import time


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for i in range(1, numRows):
            next_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    next_row.append(1)
                else:
                    next_row.append(result[-1][j-1] + result[-1][j])
            result.append(next_row)
        return result


start_time = time()

_numRows = 5
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print(Solution().generate(_numRows))

print("--- %s seconds ---" % (time() - start_time))
