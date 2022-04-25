from time import time


class Solution:
    def findMin(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        max_index = None
        while start < end:
            if nums[start] > nums[start + 1]:
                max_index = start
                break
            mid = (end + start) // 2
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
                start += 1
        if max_index is None:
            return nums[0]
        return nums[max_index + 1]

start_time = time()

_nums = [1, 2, 3, 4, 5]
_nums = [1,3,5]

print(Solution().findMin(_nums))

print("--- %s seconds ---" % (time() - start_time))
