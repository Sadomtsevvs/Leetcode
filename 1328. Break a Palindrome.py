from time import time


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        half = len(palindrome) // 2
        for i in range(half):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
            if i == half - 1:
                palindrome[-1] = 'b'
                return ''.join(palindrome)
        return ''


start_time = time()

_palindrome = "abccba"
# Example 1:
# Input: palindrome = "abccba"
# Output: "aaccba"
# Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
# Of all the ways, "aaccba" is the lexicographically smallest.
#
# Example 2:
# Input: palindrome = "a"
# Output: ""
# Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

print(Solution().breakPalindrome(_palindrome))

print("--- %s seconds ---" % (time() - start_time))
