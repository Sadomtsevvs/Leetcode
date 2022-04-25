from time import time
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        get_odd = False
        for num in Counter(s).values():
            if num % 2 == 0:
                result += num
            else:
                result += num - 1
                if not get_odd:
                    result += 1
                    get_odd = True
        return result



start_time = time()

_s = "abccccdfsgdbcgfhdfgfdhdd"
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

print(Solution().longestPalindrome(_s))

print("--- %s seconds ---" % (time() - start_time))
