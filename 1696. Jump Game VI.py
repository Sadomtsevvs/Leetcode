from collections import deque
from time import time
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        deq, n = deque([0]), len(nums)
        for i in range(1, n):
            while deq and deq[0] < i - k:
                deq.popleft()
            nums[i] += nums[deq[0]]
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
        return nums[-1]


start_time = time()

_nums = [1, 2, 3, -1,-1]
_k = 3
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
#
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
#
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0

print(Solution().maxResult(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
