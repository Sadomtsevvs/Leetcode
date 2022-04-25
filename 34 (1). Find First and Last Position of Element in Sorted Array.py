from time import time


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # first we should find if target exists in the array
        l, r = 0, len(nums) - 1
        pivot = None
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                pivot = mid
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if pivot is None:
            return [-1, -1]

        # find left border
        l, r = 0, pivot
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                r = mid - 1
            else:
                # elif nums[mid] < target:
                l = mid + 1
        lr = r + 1

        # find right border
        l, r = pivot, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                l = mid + 1
            else:
                # elif nums[mid] > target:
                r = mid - 1
        rr = l - 1

        return [lr, rr]


start_time = time()

_nums = [5,7,7,8,8,10]
_target = 8
_nums = [1, 1, 1, 1]
_target = 1

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

print(Solution().searchRange(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))
