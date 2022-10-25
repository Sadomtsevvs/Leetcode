from time import time
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        set_seen = set()
        set_correct = set(range(1, len(nums) + 1))
        for num in nums:
            if num in set_seen:
                result.append(num)
            else:
                set_correct.remove(num)
            set_seen.add(num)
        result.append(list(set_correct)[0])
        return result

        # from LC
        #
        # n, a, b = len(nums), sum(nums), sum(set(nums))
        # s = n * (n + 1) // 2
        # return [a - b, s - b]

start_time = time()

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
#
_nums = [1,1]
# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
_nums = [1,3,3]

print(Solution().findErrorNums(_nums))

print("--- %s seconds ---" % (time() - start_time))
