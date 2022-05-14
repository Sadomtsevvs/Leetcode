from time import time
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum_left = [0] * n
        sum_right = [0] * n
        sum_left[0] = nums[0]
        sum_right[n-1] = nums[n-1]
        for i in range(1, n):
            sum_left[i] = nums[i] + sum_left[i-1]
            sum_right[n-i-1] = nums[n-i-1] + sum_right[n-i]
        ans = 0
        for i in range(n-1):
            if sum_left[i] >= sum_right[i+1]:
                ans += 1
        return ans


start_time = time()

_nums = [10,4,-8,7]
_nums = [2,3,1,0]
# Input: nums = [10,4,-8,7]
# Output: 2
# Explanation:
# There are three ways of splitting nums into two non-empty parts:
# - Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
# - Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
# - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
# Thus, the number of valid splits in nums is 2.

print(Solution().waysToSplitArray(_nums))

print("--- %s seconds ---" % (time() - start_time))
