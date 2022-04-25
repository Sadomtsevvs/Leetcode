from time import time


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


start_time = time()

_nums = [4,3,2,7,8,2,3,1]
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

print(Solution().findDisappearedNumbers(_nums))

print("--- %s seconds ---" % (time() - start_time))
