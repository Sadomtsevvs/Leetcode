from time import time


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums * 2


start_time = time()

_nums = [1,2,1]
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

print(Solution().getConcatenation(_nums))

print("--- %s seconds ---" % (time() - start_time))
