from time import time


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        zeros = 0
        ones = 0
        last_zero = True
        for char in s:
            if char == '1':
                if not zeros and not ones:
                    ones += 1
                    last_zero = False
                    continue
                if last_zero and ones > 0:
                    ones = 0
                last_zero = False
                ones += 1
                if ones <= zeros:
                    ans += 1
            else:
                if not zeros and not ones:
                    zeros += 1
                    last_zero = True
                    continue
                if not last_zero and zeros > 0:
                    zeros = 0
                last_zero = True
                zeros += 1
                if zeros <= ones:
                    ans += 1
        return ans


start_time = time()

_s = "00110011"
# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
#
_s = "10101"
# Example 2:
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

print(Solution().countBinarySubstrings(_s))

print("--- %s seconds ---" % (time() - start_time))
