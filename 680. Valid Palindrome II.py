from time import time

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validPalindrome2(ss, may_delete=True):
            i = 0
            while i < len(ss) // 2:
                if ss[i] != ss[-i-1]:
                    if not may_delete:
                        return False
                    return validPalindrome2(ss[i+1:len(ss)-i], False) or validPalindrome2(ss[i:len(ss)-i-1], False)
                else:
                    i += 1
            return True

        return validPalindrome2(s)


start_time = time()

_s = "abca"
_s = "abc"
# _s = "eeccccbebaeeabebccceea"
# _s = "uucuppucu"

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

print(Solution().validPalindrome(_s))

print("--- %s seconds ---" % (time() - start_time))
