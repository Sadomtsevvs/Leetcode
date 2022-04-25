from time import time


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        # recursion is too slow
        #
        # def pascal(i, j):
        #     if i == 0 or j == 0:
        #         return 1
        #     return pascal(i, j - 1) + pascal(i - 1, j)
        #
        # result = []
        # for j in range(rowIndex + 1):
        #     result.append(pascal(rowIndex - j, j))
        #
        # return result

        # dynamic programming

        result = [[1]]  # [[1], [1,1], [1,2,1],...]

        for i in range(1, rowIndex + 1):
            next_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    next_row.append(1)
                else:
                    next_row.append(result[-1][j-1] + result[-1][j])
            result.append(next_row)

        return result[-1]

        # solution from LC comments, like mine, but with less memory
        #
        # result = [1]
        # for i in range(rowIndex):
        #     above_result = result
        #     result=[1]
        #     for j in range(1,len(above_result)):
        #         result.append(above_result[j-1]+above_result[j])
        #     result.append(1)
        # return result


start_time = time()

_rowIndex = 24

print(Solution().getRow(_rowIndex))

print("--- %s seconds ---" % (time() - start_time))
