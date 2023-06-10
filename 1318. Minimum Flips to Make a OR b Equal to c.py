from time import time


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a | b != c:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            if bit_a == 1 and bit_b == 1 and bit_c == 0:
                count += 2
            elif bit_a | bit_b != bit_c:
                count += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return count


start_time = time()

# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
_a = 2
_b = 6
_c = 5
#
# Example 2:
# Input: a = 4, b = 2, c = 7
# _a = 4
# _b = 2
# _c = 7
# Output: 1
#
# Example 3:
# Input: a = 1, b = 2, c = 3
# Output: 0

print(Solution().minFlips(_a, _b, _c))

print("--- %s seconds ---" % (time() - start_time))
