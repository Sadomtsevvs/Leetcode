from time import time


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        sign = 0 if num > 0 else 1
        num_list = list(str(num)[sign:])
        num_list.sort()
        if sign == 1:
            return - int(''.join(num_list[::-1]))
        zeros = num_list.count('0')
        if zeros > 0:
            num_list[0], num_list[zeros] = num_list[zeros], num_list[0]
        return int(''.join(num_list))


start_time = time()

_num = 3100
# _num = -7605
# Input: num = 310
# Output: 103
# Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310.
# The arrangement with the smallest value that does not contain any leading zeros is 103.

print(Solution().smallestNumber(_num))

print("--- %s seconds ---" % (time() - start_time))
