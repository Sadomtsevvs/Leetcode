from math import ceil
from time import time
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        '''
        ans = 0
        beg, end = min(nums), max(nums)
        nums = nums[::-1]
        while beg <= end:
            mid = (beg+end) // 2
            left = 0
            for num in nums:
                free = mid - num
                left -= free
                left = max(left, 0)
            if left == 0:
                ans = mid
                end = mid - 1
            else:
                beg = mid + 1
        return ans
        '''
        ans = 0
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            ans = max(ans, ceil(cur/(i+1)))
        return ans


start_time = time()


# Example 1:
# Input: nums = [3,7,1,6]
_nums = [3, 7, 1, 6]
# Output: 5
# Explanation:
# One set of optimal operations is as follows:
# 1. Choose i = 1, and nums becomes [4,6,1,6].
# 2. Choose i = 3, and nums becomes [4,6,2,5].
# 3. Choose i = 1, and nums becomes [5,5,2,5].
# The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
# Therefore, we return 5.
#
# Example 2:
# Input: nums = [10,1]
# Output: 10
# Explanation:
# It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.


print(Solution().minimizeArrayValue(_nums))

print("--- %s seconds ---" % (time() - start_time))
