from time import time


class Solution:
    def minimumLength(self, s: str) -> int:
        # I think two pointers is the best way
        beg, end = 0, len(s) - 1
        while beg < end and s[beg] == s[end]:
            while beg < end and s[beg] == s[end]:
                beg += 1
            beg -= 1
            while beg < end and s[beg] == s[end]:
                end -= 1
            beg += 1
        return end - beg + 1


start_time = time()

# Example 1:
# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.
#
# Example 2:
# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".
#
# Example 3:
# Input: s = "aabccabba"
_s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

print(Solution().minimumLength(_s))

print("--- %s seconds ---" % (time() - start_time))
