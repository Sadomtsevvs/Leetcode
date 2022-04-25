from time import time


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # find any match
        start = 0
        any_index = None
        end = len(nums) - 1
        while end >= start:
            mid = (end + start) // 2
            if nums[mid] == target:
                any_index = mid
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if any_index is None:
            return [-1, -1]
        # find left boundary
        start = 0
        end = any_index
        while end > start:
            mid = (end + start) // 2
            if nums[mid] == target:
                end = mid
            else:
                start = mid + 1
        left_boundary = end
        # find right boundary
        start = any_index
        end = len(nums) - 1
        while end > start:
            mid = (end + start) // 2 + 1
            if nums[mid] == target:
                start = mid
            else:
                end = mid - 1
        right_boundary = end
        return [left_boundary, right_boundary]

start_time = time()

_nums = [5, 7, 7, 8, 8, 10]
_target = 9

print(Solution().searchRange(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))