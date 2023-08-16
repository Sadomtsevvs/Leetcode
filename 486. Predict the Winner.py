from functools import cache
from time import time
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dp(beg, end, turn):
            if beg > end:
                return 0
            if turn:
                return max(dp(beg + 1, end, not turn) + nums[beg],
                           dp(beg, end - 1, not turn) + nums[end])
            else:
                return min(dp(beg + 1, end, not turn) - nums[beg],
                           dp(beg, end - 1, not turn) - nums[end])

        return True if dp(0, len(nums) - 1, True) >= 0 else False


start_time = time()

# Example 1:
# Input: nums = [1,5,2]
_nums = [1,5,2]
# Output: false
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return false.
#
# Example 2:
# Input: nums = [1,5,233,7]
# _nums = [1,5,233,7]
# Output: true
# Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
_nums = [1,5,233,7]

# _nums = [1,1]

print(Solution().PredictTheWinner(_nums))

print("--- %s seconds ---" % (time() - start_time))
