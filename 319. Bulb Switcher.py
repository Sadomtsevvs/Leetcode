from math import floor
from time import time


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return floor(n ** 0.5)


start_time = time()

# Example 1:
# Input: n = 3
_n = 3
# Output: 1
# Explanation: At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off].
# So you should return 1 because there is only one bulb is on.
#
# Example 2:
# Input: n = 0
# Output: 0
#
# Example 3:
# Input: n = 1
_n = 1
# Output: 1

_n = 27

print(Solution().bulbSwitch(_n))

print("--- %s seconds ---" % (time() - start_time))
