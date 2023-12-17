from time import time


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        s = str(bin(n))[2:]
        return s.count('0') + len(s)


start_time = time()

# Example 1:
# Input: n = 3
_n = 3
# Output: 2
# Explanation: The binary representation of 3 is "11".
# "11" -> "01" with the 2nd operation since the 0th bit is 1.
# "01" -> "00" with the 1st operation.
#
# Example 2:
# Input: n = 6
# _n = 6
# Output: 4
# Explanation: The binary representation of 6 is "110".
# "110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
# "010" -> "011" with the 1st operation.
# "011" -> "001" with the 2nd operation since the 0th bit is 1.
# "001" -> "000" with the 1st operation.

print(Solution().minimumOneBitOperations(_n))

print("--- %s seconds ---" % (time() - start_time))
