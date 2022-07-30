from time import time
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        # monotonic stack solution
        result = 0
        nums = [float('inf')] + nums + [float('inf')]
        stack = [0]
        for i in range(len(nums)):
            while nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                result += nums[idx] * (i-idx) * (idx-stack[-1])
            stack.append(i)
        nums[0], nums[-1] = -float('inf'), -float('inf')
        stack = [0]
        for i in range(len(nums)):
            while nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                result -= nums[idx] * (i-idx) * (idx-stack[-1])
            stack.append(i)
        return result

        # brute force O(n**2)
        #
        # result = 0
        # for left in range(len(nums) - 1):
        #     mn = mx = nums[left]
        #     for right in range(left + 1, len(nums)):
        #         num = nums[right]
        #         if num < mn:
        #             mn = num
        #         if num > mx:
        #             mx = num
        #         result += (mx - mn)
        # return result

        # little optimized but still O(n**2)
        #
        # result = 0
        # max_right = len(nums)
        # fast = False
        # mn = mx = 0
        # for left in range(len(nums) - 1):
        #     cur_mn = cur_mx = nums[left]
        #     mn_idx = mx_idx = left
        #     if fast and left > min_right:
        #         fast = False
        #         max_right = len(nums)
        #     if fast:
        #         result += (len(nums) - max_right) * (mx - mn)
        #     for right in range(left + 1, max_right):
        #         num = nums[right]
        #         if num < cur_mn:
        #             cur_mn = num
        #             mn_idx = right
        #         if num > cur_mx:
        #             cur_mx = num
        #             mx_idx = right
        #         result += (cur_mx - cur_mn)
        #     if not fast:
        #         fast = True
        #         mn = cur_mn
        #         mx = cur_mx
        #         max_right = max(mn_idx, mx_idx)
        #         min_right = min(mn_idx, mx_idx)
        # return result



start_time = time()

# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

_nums = [4, -2, -3, 4, 1]
# Input: nums = [4,-2,-3,4,1]
# Output: 59
# Explanation: The sum of all subarray ranges of nums is 59.

print(Solution().subArrayRanges(_nums))

print("--- %s seconds ---" % (time() - start_time))
