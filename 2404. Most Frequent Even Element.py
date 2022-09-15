from collections import Counter
from time import time
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ans = -1
        max_freq = 0
        cntr = Counter(nums)
        for num, freq in cntr.items():
            if num % 2 == 1:
                continue
            if freq > max_freq:
                max_freq = freq
                ans = num
            elif freq == max_freq and num < ans:
                ans = num
        return ans


start_time = time()

_nums = [0,1,2,2,4,4,1]
# Example 1:
# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.
#
# Example 2:
# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.
#
# Example 3:
# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.

print(Solution().mostFrequentEven(_nums))

print("--- %s seconds ---" % (time() - start_time))
