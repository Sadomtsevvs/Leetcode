from time import time


class Solution:
    def numTilings(self, n: int) -> int:


start_time = time()

_n = 3
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.

print(Solution().numTilings(_n))

print("--- %s seconds ---" % (time() - start_time))
