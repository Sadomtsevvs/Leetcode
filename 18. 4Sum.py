from time import time
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        n = len(nums)
        nums.sort()
        for i in range(n-3):
            num1 = nums[i]
            sum3 = target - num1
            for j in range(i+1, n-2):
                num2 = nums[j]
                sum2 = sum3 - num2
                left, right = j + 1, n - 1
                num3, num4 = nums[left], nums[right]
                while left < right:
                    if num3 + num4 == sum2:
                        result.add((num1, num2, num3, num4))
                        left += 1
                        right -= 1
                        num3, num4 = nums[left], nums[right]
                    elif num3 + num4 < sum2:
                        left += 1
                        num3 = nums[left]
                    else:
                        right -= 1
                        num4 = nums[right]
        return list(result)


start_time = time()

_nums = [1,0,-1,0,-2,2]
_target = 0
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

print(Solution().fourSum(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))