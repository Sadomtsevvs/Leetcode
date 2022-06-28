from time import time
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        prev_max = -10**5 - 1
        found_1 = False
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                prev_max = nums[i-1]
            elif not found_1:
                if prev_max > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = prev_max
                prev_max = nums[i-1]
                found_1 = True
            else:
                return False
        return True


        # wrong answer with [3,4,2,3]
        #
        # if len(nums) == 1:
        #     return True
        # found_1 = False
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i+1]:
        #         if not found_1:
        #             found_1 = True
        #         else:
        #             return False
        # return True


start_time = time()

_nums = [4,2,3]
_nums = [4,2,1]
_nums = [3,4,2,3]

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

print(Solution().checkPossibility(_nums))

print("--- %s seconds ---" % (time() - start_time))