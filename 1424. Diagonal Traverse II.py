from time import time
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        # Let's try bfs after reading the tutorial
        n = len(nums)
        ans = []
        level = [(0, 0)]
        while level:
            next_level = []
            for k in range(len(level)):
                i, j = level[k]
                ans.append(nums[i][j])
                if j == 0 and i < n - 1:
                    next_level.append((i+1, j))
                if j < len(nums[i]) - 1:
                    next_level.append((i, j+1))
            level = next_level
        return ans

        # TLE
        #
        # n = len(nums)
        # lens = [len(num) for num in nums]
        # m = max(lens)
        # cnt = sum(lens)
        # ans = []
        # for i in range(n):
        #     if len(ans) == cnt:
        #         break
        #     for ii in range(i+1):
        #         if lens[i-ii] >= ii + 1:
        #             ans.append(nums[i-ii][ii])
        #             if len(ans) == cnt:
        #                 break
        # for j in range(1, m):
        #     if len(ans) == cnt:
        #         break
        #     for i in range(n-1, -1, -1):
        #         if n - i + j - 1 > m:
        #             break
        #         if lens[i] >= n - i + j:
        #             ans.append(nums[i][n - i + j - 1])
        #             if len(ans) == cnt:
        #                 break
        # return ans


start_time = time()

# Example 1:
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
#
# Example 2:
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

_nums = [[14,12,19,16,9],
         [13,14,15,8,11],
         [11,13,1]]

print(Solution().findDiagonalOrder(_nums))

print("--- %s seconds ---" % (time() - start_time))