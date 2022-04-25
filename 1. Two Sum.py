from time import time


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        """ my hardcode solution
        for i in range(len(nums) - 1):
            seek_for = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == seek_for:
                    return [i, j]
        """

        # better solution from leetcode

        storage = {}
        for i in range(len(nums)):
            seek_for = target - nums[i]
            if seek_for in storage:
                return [storage[seek_for], i]
            storage[nums[i]] = i


start_time = time()

_numbers = [3, 2, 4]
_target = 6

print(Solution().twoSum(_numbers, _target))

print("--- %s seconds ---" % (time() - start_time))
