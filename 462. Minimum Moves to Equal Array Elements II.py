from time import time
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        # wrong algorithm
        #
        # avg = round(sum(nums) / len(nums))
        # ans = 0
        # for num in nums:
        #     ans += abs(num - avg)
        # return ans

        # let's try binary search, doesn't work
        # if len(nums) == 1:
        #     return 0
        #
        # def cnt_moves(target):
        #     a = 0
        #     for num in nums:
        #         a += abs(num - target)
        #     return a
        #
        # ans = 0
        # left = min(nums)
        # right = max(nums)
        # while right > left:
        #     n_left = cnt_moves(left)
        #     n_right = cnt_moves(right)
        #     ans = min(n_left, n_right)
        #     mid = (left + right) // 2
        #     if n_left <= n_right:
        #         right = mid
        #     elif left == mid:
        #         break
        #     else:
        #         left = mid
        # return ans

        # Pochmann solution, median
        # median = sorted(nums)[len(nums) // 2]
        # return sum(abs(num - median) for num in nums)

        # two pointers
        ans = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            ans += nums[right] - nums[left]
            left += 1
            right -= 1
        return ans



start_time = time()

_nums = [1,2,3]
_nums = [1,10,2,9]
_nums = [1,0,0,8,6]
_nums = [1,2,5,8,0]
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

print(Solution().minMoves2(_nums))

print("--- %s seconds ---" % (time() - start_time))