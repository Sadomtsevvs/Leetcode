from time import time


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


start_time = time()

_nums = [1,3,4,2]
# _nums = [1,1,1,3,3,4,3,2,4,2]
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

print(Solution().containsDuplicate(_nums))

print("--- %s seconds ---" % (time() - start_time))
