from time import time


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        # TLE
        #

        def odd_equal_ven(n):
            even, odd = 0, 0
            for char in n:
                if int(char) % 2 == 0:
                    even += 1
                else:
                    odd += 1
            return even == odd

        result = 0

        if low < k:
            num = k
        elif low % k == 0:
            num = low
        else:
            num = (low // k + 1) * k

        while num <= high:
            str_num = str(num)
            if len(str_num) % 2 == 1:
                num = 10 ** (len(str_num))
                if num % k != 0:
                    num = (num // k + 1) * k
                continue
            if odd_equal_ven(str_num):
                result += 1
            num += k

        return result


start_time = time()

# Example 1:
# Input: low = 10, high = 20, k = 3
_low = 10
_high = 20
_k = 3
# Output: 2
# Explanation: There are 2 beautiful integers in the given range: [12,18].
# - 12 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
# - 18 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
# Additionally we can see that:
# - 16 is not beautiful because it is not divisible by k = 3.
# - 15 is not beautiful because it does not contain equal counts even and odd digits.
# It can be shown that there are only 2 beautiful integers in the given range.
#
# Example 2:
# Input: low = 1, high = 10, k = 1
_low = 1
_high = 10
_k = 1
# Output: 1
# Explanation: There is 1 beautiful integer in the given range: [10].
# - 10 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 1.
# It can be shown that there is only 1 beautiful integer in the given range.
#
# Example 3:
# Input: low = 5, high = 5, k = 2
# Output: 0
# Explanation: There are 0 beautiful integers in the given range.
# - 5 is not beautiful because it is not divisible by k = 2 and it does not contain equal even and odd digits.

_low = 3
_high = 31
_k = 16

_low = 1
_high = 10
_k = 1

_low = 9
_high = 25
_k = 4

print(Solution().numberOfBeautifulIntegers(_low, _high, _k))

print("--- %s seconds ---" % (time() - start_time))
