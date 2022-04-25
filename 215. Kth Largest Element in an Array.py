from time import time
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k):
            result = heapq.heappop(heap)
        return -result


start_time = time()

_nums = [3,2,3,1,2,4,5,5,6]
_k = 4
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

print(Solution().findKthLargest(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
