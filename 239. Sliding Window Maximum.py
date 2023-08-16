import heapq
from time import time
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []

        heap = []
        heapq.heapify(heap)

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])

        return ans


start_time = time()

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
_nums = [1, 3, -1, -3, 5, 3, 6, 7]
_k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

print(Solution().maxSlidingWindow(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
