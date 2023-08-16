from functools import cache
from time import time
from typing import List


class Solution:

    def __init__(self):
        self.powers = ['1', '101', '11001', '1111101', '1001110001', '110000110101', '11110100001001']

    def minimumBeautifulSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return -1
        ans = 16
        for power in self.powers:
            if len(power) <= len(s) and s[:len(power)] == power:
                next_s = self.minimumBeautifulSubstrings(s[len(power):])
                if next_s != -1:
                    ans = min(ans, 1 + next_s)
        return ans if ans < 16 else -1


start_time = time()

# Example 1:
# Input: s = "1011"
_s = "1011"
# Output: 2
# Explanation: We can paritition the given string into ["101", "1"].
# - The string "101" does not contain leading zeros and is the binary representation of integer 51 = 5.
# - The string "1" does not contain leading zeros and is the binary representation of integer 50 = 1.
# It can be shown that 2 is the minimum number of beautiful substrings that s can be partitioned into.
#
# Example 2:
# Input: s = "111"
# _s = "111"
# Output: 3
# Explanation: We can paritition the given string into ["1", "1", "1"].
# - The string "1" does not contain leading zeros and is the binary representation of integer 50 = 1.
# It can be shown that 3 is the minimum number of beautiful substrings that s can be partitioned into.
#
# Example 3:
# Input: s = "0"
# _s = "0"
# Output: -1
# Explanation: We can not partition the given string into beautiful substrings.

# _s = "111111101"

print(Solution().minimumBeautifulSubstrings(_s))

print("--- %s seconds ---" % (time() - start_time))
