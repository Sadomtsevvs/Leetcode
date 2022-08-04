from time import time


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        dic = {1000: ('_', '_', 'M'), 100: ('M', 'D', 'C'), 10: ('C', 'L', 'X'), 1: ('X', 'V', 'I')}
        rank = 1000
        while num > 0:
            res, num = divmod(num, rank)
            if res == 9:
                ans += dic[rank][2] + dic[rank][0]
            elif res == 4:
                ans += dic[rank][2] + dic[rank][1]
            else:
                if res >= 5:
                    ans += dic[rank][1]
                    res -= 5
                ans += res * dic[rank][2]
            rank //= 10
        return ans

        # solution from LC
        #
        # values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # res = ""
        # for i, v in enumerate(values):
        #     res += (num // v) * numerals[i]
        #     num %= v
        # return res

        # official solution
        #
        # digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
        #           (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
        #           (5, "V"), (4, "IV"), (1, "I")]
        # roman_digits = []
        # # Loop through each symbol.
        # for value, symbol in digits:
        #     # We don't want to continue looping if we're done.
        #     if num == 0: break
        #     count, num = divmod(num, value)
        #     # Append "count" copies of "symbol" to roman_digits.
        #     roman_digits.append(symbol * count)
        # return "".join(roman_digits)

start_time = time()


# Example 1:
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
#
# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
_num = 1994
_num = 2554
# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

print(Solution().intToRoman(_num))

print("--- %s seconds ---" % (time() - start_time))
