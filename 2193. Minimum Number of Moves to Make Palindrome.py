from time import time


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # after reading comments
        res = 0
        s = list(s)
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1:
                res += i // 2
            else:
                res += i
                s.pop(i)
            s.pop()
        return res


start_time = time()

_s = "aabb"
# Example 1:
# Input: s = "aabb"
# Output: 2
# Explanation:
# We can obtain two palindromes from s, "abba" and "baab".
# - We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
# - We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
# Thus, the minimum number of moves needed to make s a palindrome is 2.
#
# Example 2:
# Input: s = "letelt"
# Output: 2
# Explanation:
# One of the palindromes we can obtain from s in 2 moves is "lettel".
# One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
# Other palindromes such as "tleelt" can also be obtained in 2 moves.
# It can be shown that it is not possible to obtain a palindrome in less than 2 moves.

print(Solution().minMovesToMakePalindrome(_s))

print("--- %s seconds ---" % (time() - start_time))
