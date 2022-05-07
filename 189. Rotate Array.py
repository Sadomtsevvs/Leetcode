from time import time


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # O(1) space solution (in-place) from LC comments
    #
    # reverse the first n - k elements
    # reverse the rest of them
    # reverse the entire array
    #
    # def rotate(self, nums, k):
    #     if k is None or k <= 0:
    #         return
    #     k, end = k % len(nums), len(nums) - 1
    #     self.reverse(nums, 0, end - k)
    #     self.reverse(nums, end - k + 1, end)
    #     self.reverse(nums, 0, end)
    #
    # def reverse(self, nums, start, end):
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start, end = start + 1, end - 1

    # another solution
    #
    # n, k, j = len(nums), k % len(nums), 0
    # while n > 0 and k % n != 0:
    #     for i in xrange(0, k):
    #         nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i]  # swap
    #     n, j = n - k, j + k
    #     k = k % n


start_time = time()

_nums = [1, 2, 3, 4, 5, 6, 7]
_k = 3
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

Solution().rotate(_nums, _k)

print(_nums)

print("--- %s seconds ---" % (time() - start_time))
