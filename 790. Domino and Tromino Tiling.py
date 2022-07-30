from time import time


class Solution:
    def numTilings(self, n: int) -> int:

        # after reading official solution
        #
        if n == 1:
            return 1
        full = [0] * n
        full[0] = 1
        full[1] = 2
        part = [0] * n
        part[0] = 0
        part[1] = 1
        for i in range(2, n):
            full[i] = full[i-1] + full[i-2] + 2 * part[i-1]
            part[i] = full[i-2] + part[i-1]
        return full[-1] % (10**9 + 7)



start_time = time()

_n = 3
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.

print(Solution().numTilings(_n))

print("--- %s seconds ---" % (time() - start_time))
