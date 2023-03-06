from time import time


class Solution:
    def splitNum(self, num: int) -> int:
        chars = [char for char in str(num) if char != '0']
        chars.sort()
        num1, num2 = '0', '0'
        for i in range(len(chars)):
            if i % 2 == 0:
                num1 += chars[i]
            else:
                num2 += chars[i]
        return int(num1) + int(num2)


start_time = time()

_num = 4325
# Example 1:
# Input: num = 4325
# Output: 59
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
#
_num = 687
# Example 2:
# Input: num = 687
# Output: 75
# Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75.

_num = 10

print(Solution().splitNum(_num))

print("--- %s seconds ---" % (time() - start_time))
