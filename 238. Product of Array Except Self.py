from time import time


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left, right = [1] * n, [1] * n
        left[0], right[-1] = nums[0], nums[-1]
        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
            right[n-i-1] = right[n-i] * nums[n-i-1]
        return [right[1]] + [left[i-1] * right[i+1] for i in range(1, n-1)] + [left[-2]]

        # left_prod = [nums[0]]
        # for i in range(1, len(nums)):
        #     left_prod.append(left_prod[i-1] * nums[i])
        # right_prod = [nums[-1]] * len(nums)
        # for i in range(len(nums)-2, -1, -1):
        #     right_prod[i] = right_prod[i+1] * nums[i]
        # result = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         result.append(right_prod[1])
        #     elif i == len(nums) - 1:
        #         result.append(left_prod[len(nums)-2])
        #     else:
        #         result.append(left_prod[i-1] * right_prod[i+1])
        # return result

        # amazing solution from LC comment
        # preparing left and rignt in the result answer
        #
        # ans, suf, pre = [1] * len(nums), 1, 1
        # for i in range(len(nums)):
        #     ans[i] *= pre  # prefix product from one end
        #     pre *= nums[i]
        #     ans[-1 - i] *= suf  # suffix product from other end
        #     suf *= nums[-1 - i]
        # return ans


start_time = time()


_nums = [1,2,3,4]
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

print(Solution().productExceptSelf(_nums))

print("--- %s seconds ---" % (time() - start_time))
