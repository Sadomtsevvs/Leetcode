from time import time


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        return True

        # from LC comments
        #
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if not s[l].isalnum():
        #         l += 1
        #     elif not s[r].isalnum():
        #         r -= 1
        #     else:
        #         if s[l].lower() != s[r].lower():
        #             return False
        #         else:
        #             l += 1
        #             r -= 1
        # return True


start_time = time()

_s = "A man, a plan, a canal: Panama"
_s = "race a car"
_s = "   "
_s = "0P"
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

print(Solution().isPalindrome(_s))

print("--- %s seconds ---" % (time() - start_time))
