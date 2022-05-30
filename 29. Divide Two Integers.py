from time import time


# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = True
        if dividend < 0:
            dividend = 0 - dividend
            sign = not sign
        if divisor < 0:
            divisor = 0 - divisor
            sign = not sign

        if divisor > dividend:
            return 0
        elif divisor == 1:
            result = dividend
        else:
            cur_dividend = 0
            result = 0
            while cur_dividend + divisor <= dividend:
                d = divisor
                cnt = 1
                while cur_dividend + d**cnt <= dividend:
                    cnt += 1
                cur_dividend += d**(cnt-1)
                result += d**(cnt-2)

        result = result if sign else 0 - result
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < - 2**31:
            return - 2**31
        return result

        # from LC comments, great
        #
        # positive = (dividend < 0) is (divisor < 0)
        # dividend, divisor = abs(dividend), abs(divisor)
        # res = 0
        # while dividend >= divisor:
        #     temp, i = divisor, 1
        #     while dividend >= temp:
        #         dividend -= temp
        #         res += i
        #         i <<= 1
        #         temp <<= 1
        # if not positive:
        #     res = -res
        # return min(max(-2147483648, res), 2147483647)


start_time = time()

# _dividend = 7
# _divisor = -3
# _dividend = 1
# _divisor = 1
_dividend = 10
_divisor = 3
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Input
# -2147483648
# -1
# Output
# 2147483648
# Expected
# 2147483647

print(Solution().divide(_dividend, _divisor))

print("--- %s seconds ---" % (time() - start_time))
