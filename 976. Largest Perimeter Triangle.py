from time import time
from heapq import *


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        heap = [-n for n in nums]
        heapify(heap)
        a, b, c, = -heappop(heap), -heappop(heap), -heappop(heap)
        while a >= b + c and heap:
            a, b, c = b, c, -heappop(heap)
        return a + b + c if a < b + c else 0

        # official solution
        #
        # A.sort()
        # for i in xrange(len(A) - 3, -1, -1):
        #     if A[i] + A[i+1] > A[i+2]:
        #         return A[i] + A[i+1] + A[i+2]
        # return 0


start_time = time()

_nums = [2,1,2]

# Input: nums = [2,1,2]
# Output: 5
#
# Input: nums = [1,2,1]
# Output: 0

# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of
# these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

print(Solution().largestPerimeter(_nums))

print("--- %s seconds ---" % (time() - start_time))
