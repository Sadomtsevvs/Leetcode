from time import time


class Solution:
    def reverseWords(self, s: str) -> str:
        # my first solution
        #
        # s = s.split()
        # return ' '.join(s[i] for i in range(len(s) - 1, -1, -1))
        return ' '.join(reversed(s.split()))


start_time = time()

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
#
_s = "a good   example"
# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

print(Solution().reverseWords(_s))

print("--- %s seconds ---" % (time() - start_time))
