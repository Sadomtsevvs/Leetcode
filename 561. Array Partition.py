from time import time
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # my first heap solution
        #
        # result = 0
        # heapq.heapify(nums)
        # while nums:
        #     result += heapq.heappop(nums)
        #     heapq.heappop(nums)
        # return result

        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result


start_time = time()

# Example 1:
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.
#
_nums = [6,2,6,5,1,2]
# Example 2:
# Input: nums = [6,2,6,5,1,2]
# Output: 9
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

print(Solution().arrayPairSum(_nums))

print("--- %s seconds ---" % (time() - start_time))
