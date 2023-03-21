from time import time
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        cur_zeroes = 0
        for num in nums:
            if num == 0:
                cur_zeroes += 1
            else:
                result += cur_zeroes * (cur_zeroes + 1) // 2
                cur_zeroes = 0
        result += cur_zeroes * (cur_zeroes + 1) // 2
        return result

        # my first solution
        #
        # ans = 0
        # first_zero = None
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         if first_zero is None:
        #             first_zero = i
        #     elif first_zero is not None:
        #         zeros = i - first_zero
        #         ans += zeros * (zeros + 1) // 2
        #         first_zero = None
        # if nums[-1] == 0:
        #     zeros = i - first_zero + 1
        #     ans += zeros * (zeros + 1) // 2
        # return ans


start_time = time()

# Example 1:
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation:
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
#
_nums = [0,0,0,2,0,0]
# Example 2:
# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
#
# Example 3:
# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.

print(Solution().zeroFilledSubarray(_nums))

print("--- %s seconds ---" % (time() - start_time))
