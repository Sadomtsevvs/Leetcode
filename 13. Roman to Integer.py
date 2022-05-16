from time import time


class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = 1000
        for char in s:
            if maps[char] > prev:
                result -= prev * 2
            prev = maps[char]
            result += maps[char]
        return result


start_time = time()

_s = "MCMXCIV"
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

print(Solution().romanToInt(_s))

print("--- %s seconds ---" % (time() - start_time))