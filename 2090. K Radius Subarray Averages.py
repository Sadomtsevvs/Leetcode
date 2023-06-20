from time import time
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            if i > 2*k:
                cur -= nums[i-2*k-1]
            if i >= 2*k:
                ans.append(cur // (2*k+1))
            elif i < k:
                ans.append(-1)
        for i in range(len(nums) - len(ans)):
            ans.append(-1)
        return ans


start_time = time()

# Example 1:
# Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
_nums = [7,4,3,9,1,8,5,2,6]
_k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]
# Explanation:
# - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
# - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
#   Using integer division, avg[3] = 37 / 7 = 5.
# - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
# - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
# - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
#
# Example 2:
# Input: nums = [100000], k = 0
# _nums = [100000]
# _k = 0
# Output: [100000]
# Explanation:
# - The sum of the subarray centered at index 0 with radius 0 is: 100000.
#   avg[0] = 100000 / 1 = 100000.
#
# Example 3:
# Input: nums = [8], k = 100000
_nums = [8]
_k = 100000
# Output: [-1]
# Explanation:
# - avg[0] is -1 because there are less than k elements before and after index 0.

print(Solution().getAverages(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
