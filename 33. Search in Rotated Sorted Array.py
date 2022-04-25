from time import time


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # first we have to find pivot index (max index)
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
            max_index = len(nums) - 1

        start = (max_index + 1) % len(nums)
        end = max_index
        while end != start:
            if start > end:
                mid = (start + end + len(nums)) // 2 % len(nums)
            else:
                mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = (mid + 1) % len(nums)
            else:
                end = mid
        return end if nums[end] == target else -1

        # solution from LC comments
        #
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     # if found target value, return the index
        #     if nums[mid] == target:
        #         return mid
        #
        #     # determine it's left rotated or right rotated
        #     """
        #     No rotated:
        #     1 2 3 4 5 6 7
        #          mid
        #
        #     left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
        #     3 4 5 6 7 1 2
        #          mid
        #     search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
        #
        #     right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
        #     6 7 1 2 3 4 5
        #          mid
        #     search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
        #     """
        #     if nums[mid] >= nums[left]:  # left rotated
        #         # in ascending order side
        #         if nums[left] <= target and target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     else:  # right rotated
        #         # in ascending order side
        #         if nums[mid] < target and target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # # cannot find the target value
        # return -1


start_time = time()

_nums = [1]
_target = 1

print(Solution().search(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))
