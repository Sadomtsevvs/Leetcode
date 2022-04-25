from time import time


class Solution:
    def findMin(self, nums: list[int]) -> int:
        # start, end = 0, len(nums) - 1
        # max_index = None
        # while start < end:
        #     if nums[start] > nums[start + 1]:
        #         max_index = start
        #         break
        #     mid = (end + start) // 2
        #     if nums[mid] >= nums[start]:
        #         if nums[mid] < nums[end]:
        #             break
        #         start = mid
        #     else:
        #         end = mid
        #         start += 1
        # if max_index is None:
        #     return nums[0]
        # return nums[max_index + 1]

        if len(nums) == 1:
            return nums[0]

        start, end = 0, len(nums) - 1
        max_index = None
        while start < end:
            mid = (end + start) // 2
            if nums[mid] > nums[mid + 1]:
                max_index = mid
                break
            if nums[mid] == nums[start] and nums[mid] == nums[end] and start == 0 and end == len(nums) - 1:
                return min(self.findMin(nums[start:mid+1]), self.findMin(nums[mid+1:end+1]))
            elif nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
        if max_index is None:
            return nums[0]
        return nums[max_index + 1]

        # solution from lc comments
        #
        # lo, hi = 0, len(nums) - 1
        # while lo < hi:
        #     mid = lo + (hi - lo) / 2
        #     if nums[mid] > nums[hi]:
        #         lo = mid + 1
        #     else:
        #         hi = mid if nums[hi] != nums[mid] else hi - 1
        # return nums[lo]


start_time = time()

_nums = [2,2,2,0,1]
_nums = [1,3,5]
_nums = [3,1,3]
_nums = [1,1]
_nums = [3,3,1,3]
_nums = [10,1,10,10,10]
_nums = [1,3,3,3]
# Input: nums = [2,2,2,0,1]
# Output: 0

print(Solution().findMin(_nums))

print("--- %s seconds ---" % (time() - start_time))
