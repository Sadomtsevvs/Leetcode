from time import time


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l

        # previous solution
        #
        # def search(nms, start, end):
        #     if start == end:
        #         return start
        #     mid = (start + end) // 2
        #     if nms[mid] > nms[mid + 1]:
        #         return search(nms, start, mid)
        #     return search(nms, mid + 1, end)
        #
        # return search(nums, 0, len(nums) - 1)


start_time = time()

_nums = [1,2,1,3,5,6,4]
_nums = [3,4,1]
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

print(Solution().findPeakElement(_nums))

print("--- %s seconds ---" % (time() - start_time))
