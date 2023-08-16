from functools import cache
from time import time
from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = 1
        cur = 1
        prev = nums[0]
        sign = True
        for i in range(1, len(nums)):
            num = nums[i]
            if num - prev == 1 and sign:
                cur += 1
                sign = False
                ans = max(ans, cur)
            elif num - prev == -1 and not sign:
                cur += 1
                sign = True
                ans = max(ans, cur)
            elif num - prev == 1:
                cur = 2
                sign = False
            else:
                cur = 1
                sign = True
            prev = num
        return -1 if ans == 1 else ans


start_time = time()

# Example 1:
# Input: nums = [2,3,4,3,4]
_nums = [2,3,4,3,4]
# Output: 4
# Explanation: The alternating subarrays are [3, 4], [3, 4, 3], and [3, 4, 3, 4]. The longest of these is [3,4,3,4], which is of length 4.
#
# Example 2:
# Input: nums = [4,5,6]
_nums = [4,5,6]
# Output: 2
# Explanation: [4,5] and [5,6] are the only two alternating subarrays. They are both of length 2.

print(Solution().alternatingSubarray(_nums))

print("--- %s seconds ---" % (time() - start_time))
