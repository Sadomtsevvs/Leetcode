from time import time
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        result = 0
        for num in nums:
            if num:
                cur += 1
                result = max(result, prev + cur)
            else:
                prev, cur = cur, 0
        return result - (result == len(nums))


start_time = time()

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
#
_nums = [0,1,1,1,0,1,1,0,1]
# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
#
# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.


print(Solution().longestSubarray(_nums))

print("--- %s seconds ---" % (time() - start_time))
