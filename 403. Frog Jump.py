from functools import cache
from time import time
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        last_stone = stones[-1]
        stones = set(stones)

        @cache
        def dp(i, k):
            if i == last_stone:
                return True
            if k == 0:
                return False
            if i not in stones:
                return False
            return dp(i + k + 1, k + 1) or dp(i + k, k) or dp(i + k - 1, k - 1)

        return dp(0, 1)


start_time = time()

# Example 1:
# Input: stones = [0,1,3,5,6,8,12,17]
_stones = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone,
# then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
#
# Example 2:
# Input: stones = [0,1,2,3,4,8,9,11]
_stones = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

_stones = [0,2]

print(Solution().canCross(_stones))

print("--- %s seconds ---" % (time() - start_time))
