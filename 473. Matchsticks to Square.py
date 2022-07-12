from functools import cache
from time import time
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        max_side, remainder = divmod(sum(matchsticks), 4)
        if remainder != 0:
            return False

        matchsticks.sort(reverse=True)

        @cache
        def bt(s1, s2, s3, s4, i):
            if s1 > max_side or s2 > max_side or s3 > max_side or s4 > max_side:
                return False
            if s1 == s2 == s3 == s4 == max_side and i == len(matchsticks):
                return True
            if bt(s1 + matchsticks[i], s2, s3, s4, i + 1):
                return True
            if bt(s1, s2 + matchsticks[i], s3, s4, i + 1):
                return True
            if bt(s1, s2, s3 + matchsticks[i], s4, i + 1):
                return True
            if bt(s1, s2, s3, s4 + matchsticks[i], i + 1):
                return True
            return False

        return bt(0, 0, 0, 0, 0)


start_time = time()

_matchsticks = [1,1,2,2,2]
# Example 1:
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

# Example 2:
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.

print(Solution().makesquare(_matchsticks))

print("--- %s seconds ---" % (time() - start_time))
