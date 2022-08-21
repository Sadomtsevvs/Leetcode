from time import time
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # arrays, array = [], []
        # prev_num = 0
        # for num in nums:
        #     if num != 0:
        #         if prev_num == 0:
        #             array = [num]
        #         else:
        #             array += [num]
        #     elif array:
        #         arrays.append(array.copy())
        #         array.clear()
        #     prev_num = num
        # if array:
        #     arrays.append(array.copy())
        # if len(arrays) == 0:
        #     return 0
        # if len(arrays) > 1:
        #     result = 0
        #     for array in arrays:
        #         result = max(result, self.getMaxLen(array))
        #     return result
        # nums = arrays[0]
        # prod = 1
        # nearest_minus = float('inf')
        # for i, num in enumerate(nums):
        #     if num < 0:
        #         prod = -prod
        #         nearest_minus = min(i + 1, len(nums) - i, nearest_minus)
        # if prod > 0:
        #     return len(nums)
        # if len(nums) == 1:
        #     return 0
        # return len(nums) - nearest_minus

        # from LC comments
        # 
        n = len(nums)
        pos, neg = 0, 0
        if nums[0] > 0:
            pos = 1
        if nums[0] < 0:
            neg = 1
        ans = pos
        for i in range(1, n):
            if nums[i] > 0:
                pos = 1 + pos
                neg += 1 if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans


start_time = time()

_nums = [1,-2,-3,4]
# Example 1:
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.
#
_nums = [0,1,-2,-3,-4]
# Example 2:
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
#
_nums = [-1,-2,-3,0,1]
# Example 3:
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

# _nums = [1,2,3,5,-6,4,0,10]
# Output 5
# Expected 4

_nums = [-1,1,1,-1,0,1,-1,-1]


print(Solution().getMaxLen(_nums))

print("--- %s seconds ---" % (time() - start_time))