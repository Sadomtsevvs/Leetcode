from time import time


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9


start_time = time()

# Example 1:
# Input: num = 38
_num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
#
# Example 2:
# Input: num = 0
# Output: 0

print(Solution().addDigits(_num))

print("--- %s seconds ---" % (time() - start_time))
