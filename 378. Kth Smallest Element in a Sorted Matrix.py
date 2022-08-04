from time import time


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:

        def count_elements_le_than_x(x):
            result = 0
            row, col = 0, len(matrix) - 1
            while row < len(matrix) and col >= 0:
                if matrix[row][col] <= x:
                    result += (col + 1)
                    row += 1
                else:
                    col -= 1
            return result

        ans = 0
        beg, end = matrix[0][0], matrix[-1][-1]
        while beg <= end:
            mid = (beg + end) // 2
            if count_elements_le_than_x(mid) >= k:
                ans = mid
                end = mid - 1
            else:
                beg = mid + 1
        return ans

        # # solution from LC comments, I can't solve better than O(n^2)
        #
        # n, m = len(matrix), len(matrix[0])
        #
        # def CountLessOrEqual_x(x):
        #     result = 0
        #     col = m - 1
        #     for r in range(n):
        #         while matrix[r][col] > x and col >= 0:
        #             col -= 1
        #         result += (col + 1)
        #     return result
        #
        # ans = 0
        # left, right = matrix[0][0], matrix[-1][-1]
        # while left <= right:
        #     mid = (left + right) // 2
        #     if CountLessOrEqual_x(mid) >= k:
        #         ans = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return ans


start_time = time()

_matrix = [[1,5,9],[10,11,13],[12,13,15]]
_k = 8
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

_matrix = [[1,2],[1,3]]
_k = 3

_matrix = [[2,2],[2,3]]
_k = 3

print(Solution().kthSmallest(_matrix, _k))

print("--- %s seconds ---" % (time() - start_time))
