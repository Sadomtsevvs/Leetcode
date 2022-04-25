from time import time


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        prev = None
        for i in range(len(nums)):
            if nums[i] != prev:
                nums[k] = nums[i]
                k += 1
                prev = nums[i]
        return k


start_time = time()

_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

Solution().removeDuplicates(_nums)
print(_nums)

print("--- %s seconds ---" % (time() - start_time))