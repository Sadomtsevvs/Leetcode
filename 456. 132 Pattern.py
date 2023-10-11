from time import time
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        # second solution
        #
        if len(nums) < 3:
            return False
        abs_min, abs_max = nums[0], nums[0]
        diaps = [[abs_min, abs_max]]
        for i in range(1, len(nums)):
            for n in range(len(diaps)):
                n1, n3 = diaps[n]
                if n1 < nums[i] < n3:
                    return True
                if n1 < nums[i] and n3 < nums[i]:
                    diaps[n][1] = nums[i]
            if nums[i] > abs_max:
                abs_max = nums[i]
                diaps = [[abs_min, abs_max]]
            if nums[i] < abs_min:
                abs_min = nums[i]
                diaps.append([abs_min, abs_min])
        return False

        # first solution, TLE
        #
        # if len(nums) < 3:
        #     return False
        # cur_min, cur_max = nums[0], nums[0]
        # stack = []
        # for i in range(1, len(nums)):
        #     if cur_max > nums[i] > cur_min:
        #         for num1, num3 in stack:
        #             if num3 > nums[i] > num1:
        #                 return True
        #     if nums[i] > cur_max:
        #         stack = [[cur_min, nums[i]]]
        #     elif stack and nums[i] > stack[-1][1]:
        #         stack[-1][1] = nums[i]
        #     elif nums[i] > cur_min:
        #         stack.append([cur_min, nums[i]])
        #     cur_min = min(cur_min, nums[i])
        #     cur_max = max(cur_max, nums[i])
        # return False

        # from LC comments, seeking pattern 231 instead of 132
        #
        # s2 = -float('inf')
        # stack = []
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] < s2:
        #         return True
        #     while stack and nums[i] > stack[-1]:
        #         s2 = stack.pop()
        #     stack.append(nums[i])
        # return False


start_time = time()

_nums = [3,1,4,2]
# _nums = [1,2,3,4]
# _nums = [-1,3,2,0]
# _nums = [1,0,3,-4,2]
# _nums = [1,4,0,-1,-2,-3,-1,22]
# _nums = [1,3,2,4,5,6,7,8,9,10]
_nums = [3,5,0,3,4]
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

print(Solution().find132pattern(_nums))

print("--- %s seconds ---" % (time() - start_time))
