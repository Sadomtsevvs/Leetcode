import heapq
from time import time
from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        ans = abs(nums[1] - nums[0])
        heapq.heapify(nums)
        first = heapq.heappop(nums)
        while nums:
            second = heapq.heappop(nums)
            ans = min(ans, second - first)
            first = second
        return ans


start_time = time()

# Example 1:
# Input: nums = [1,3,2,4]
_nums = [1, 3, 2, 4]
# Output: 1
# Explanation: We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
# - The maximum element of the array nums1 is equal to 2.
# - The minimum element of the array nums2 is equal to 3.
# The value of the partition is |2 - 3| = 1.
# It can be proven that 1 is the minimum value out of all partitions.
#
# Example 2:
# Input: nums = [100,1,10]
# Output: 9
# Explanation: We can partition the array nums into nums1 = [10] and nums2 = [100,1].
# - The maximum element of the array nums1 is equal to 10.
# - The minimum element of the array nums2 is equal to 1.
# The value of the partition is |10 - 1| = 9.
# It can be proven that 9 is the minimum value out of all partitions.

print(Solution().findValueOfPartition(_nums))

print("--- %s seconds ---" % (time() - start_time))
