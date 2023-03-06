from time import time


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)


start_time = time()

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
#
_n = 2
# Example 2:
# Input: n = 2
# Output: 5
# Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5.
_n = 5

print(Solution().coloredCells(_n))

print("--- %s seconds ---" % (time() - start_time))
