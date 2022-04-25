from time import time


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end >= start:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if start == end:
                    return start + 1
                start = mid + 1
            else:
                if start == end:
                    return start
                end = mid


start_time = time()

_nums = [1, 3]
_target = 2

print(Solution().searchInsert(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))
