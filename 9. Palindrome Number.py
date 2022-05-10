from time import time
from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = []
        while x > 0:
            a, b = divmod(x, 10)
            arr.append(b)
            x = a
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr)-i-1]:
                return False
        return True

        # official solution
        #
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        # reverted_number = 0
        # while x > reverted_number:
        #     a, b = divmod(x, 10)
        #     reverted_number = reverted_number * 10 + b
        #     x = a
        # return x == reverted_number or x == reverted_number // 10


start_time = time()

_x = 121
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

print(Solution().isPalindrome(_x))

print("--- %s seconds ---" % (time() - start_time))
