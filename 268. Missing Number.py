from time import time
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = sum(i for i in range(len(nums) + 1))
        for num in nums:
            ans -= num
        return ans

        # from LC
        #
        # return reduce(operator.xor, nums + range(len(nums) + 1))


start_time = time()

_nums = [9,6,4,2,3,5,7,0,1]
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
# 8 is the missing number in the range since it does not appear in nums.

print(Solution().missingNumber(_nums))

print("--- %s seconds ---" % (time() - start_time))
