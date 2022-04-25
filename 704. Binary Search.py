from time import time


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end >= start:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1



start_time = time()

_nums = [5]
_target = 5

print(Solution().search(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))
