from time import time
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # sort_nums = sorted(nums)
        # beg = len(nums)
        # end = -1
        # for i in range(len(nums)):
        #     if sort_nums[i] != nums[i]:
        #         beg = min(beg, i)
        #         end = max(end, i)
        # return 0 if end == -1 else end - beg + 1

        #  solution from LC comments
        #
        # mx = -float('inf')
        # mn = float('inf')
        # left, right = 0, len(nums) - 1
        # beg, end = -1, -1
        # while right >= 0:
        #     if nums[left] < mx:
        #         end = left
        #     else:
        #         mx = nums[left]
        #     if nums[right] > mn:
        #         beg = right
        #     else:
        #         mn = nums[right]
        #     left += 1
        #     right -= 1
        # return 0 if beg == -1 else end - beg + 1

        left = len(nums)
        right = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        return 0 if right == 0 else right - left + 1


start_time = time()

_nums = [2,6,4,8,10,9,15]
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

print(Solution().findUnsortedSubarray(_nums))

print("--- %s seconds ---" % (time() - start_time))
