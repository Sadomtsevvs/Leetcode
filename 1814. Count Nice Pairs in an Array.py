from collections import Counter
from time import time
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        for i, num in enumerate(nums):
            nums[i] -= int(str(num)[::-1])
        ans = 0
        for num in Counter(nums).values():
            ans += num * (num - 1) // 2
            ans %= MOD
        return(ans)


start_time = time()

# Example 1:
# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
#
# Example 2:
# Input: nums = [13,10,35,24,76]
_nums = [13,10,35,24,76]
# Output: 4

print(Solution().countNicePairs(_nums))

print("--- %s seconds ---" % (time() - start_time))