from time import time
from math import log, ceil


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        for i in range(1, n + 1):
            result <<= ceil(log(i+1, 2))
            result ^= i
            result %= MOD
        return result

        # official solution 1
        #
        # MOD = 10**9 + 7
        # concatenation = "".join(bin(i)[2:] for i in range(n + 1))
        # return int(concatenation, 2) % MOD

        # official solution 3, i & (i - 1) instead og log function
        #
        # MOD = 10**9 + 7
        # length = 0  # bit length of addends
        # result = 0   # long accumulator
        # for i in range(1, n + 1):
        #     # when meets power of 2, increase the bit length
        #     if i & (i - 1) == 0:
        #         length += 1
        #     result = ((result << length) | i) % MOD
        # return result


start_time = time()

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: "1" in binary corresponds to the decimal value 1.
#
_n = 3
# Example 2:
# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal value 27.
#
_n = 12
# Example 3:
# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 109 + 7, the result is 505379714.

print(Solution().concatenatedBinary(_n))

print("--- %s seconds ---" % (time() - start_time))
