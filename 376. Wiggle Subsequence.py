from time import time
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        prev = nums[0]
        wait_big = None
        for num in nums:
            if num > prev:
                if wait_big is None or wait_big:
                    ans += 1
                    wait_big = False
            elif num < prev:
                if not wait_big:
                    ans += 1
                    wait_big = True
            prev = num
        return ans


start_time = time()

_nums = [1,7,4,9,2,5]
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

_nums = [1,17,5,10,13,15,10,5,16,8]
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length.
# One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

print(Solution().wiggleMaxLength(_nums))

print("--- %s seconds ---" % (time() - start_time))
