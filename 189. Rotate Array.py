from time import time


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


start_time = time()

_nums = [-1, -100, 3, 99]
_k = 2

Solution().rotate(_nums, _k)

print(_nums)

print("--- %s seconds ---" % (time() - start_time))
