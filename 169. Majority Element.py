from time import time
from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

        # official solution
        #
        # count = 0
        # candidate = None
        #
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)
        #
        # return candidate


start_time = time()

_nums = [2,2,1,1,1,2,2]
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

print(Solution().majorityElement(_nums))

print("--- %s seconds ---" % (time() - start_time))
