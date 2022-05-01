from time import time
from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:

        seen = set()

        div_idxs = []
        div_pointer = 0
        first_idx = 0
        for i in range(len(nums)):
            if nums[i] % p == 0:
                div_idxs.append(i)
                if len(div_idxs) > k:
                    first_idx = div_idxs[div_pointer] + 1
                    div_pointer += 1
            for j in range(first_idx, i + 1):
                seen.add(tuple(nums[j:i+1]))

        return len(seen)


start_time = time()

_nums = [2,3,3,2,2]
_k = 2
_p = 2
# _nums = [1,2,3,4]
# _k = 4
# _p = 1
# Input: nums = [2,3,3,2,2], k = 2, p = 2
# Output: 11
# Explanation:
# The elements at indices 0, 3, and 4 are divisible by p = 2.
# The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
# [2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
# Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
# The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.

print(Solution().countDistinct(_nums, _k, _p))

print("--- %s seconds ---" % (time() - start_time))
