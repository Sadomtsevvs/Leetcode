from time import time
from typing import List
import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        cur_consecutive = 1
        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        while nums:
            cur = heapq.heappop(nums)
            diff = cur - prev
            if diff == 1:
                cur_consecutive += 1
                ans = max(ans, cur_consecutive)
            elif diff > 1:
                cur_consecutive = 1
            prev = cur
        return ans


start_time = time()

_nums = [100,4,200,1,3,2]
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

_nums = [0,3,7,2,5,8,4,6,0,1]
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

print(Solution().longestConsecutive(_nums))

print("--- %s seconds ---" % (time() - start_time))
