from time import time


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_h = len(haystack)
        len_n = len(needle)
        for i in range(len_h - len_n + 1):
            n_pointer = 0
            h_pointer = i
            while n_pointer < len_n and haystack[h_pointer] == needle[n_pointer]:
                h_pointer += 1
                n_pointer += 1
            if n_pointer == len_n:
                return i
        return -1

        # my second solution
        #
        # h, n = 0, 0
        # while h < len(haystack):
        #     s = h
        #     n = 0
        #     while haystack[s] == needle[n] and s < len(haystack) and n < len(needle):
        #         s += 1
        #         n += 1
        #     if n == len(needle):
        #         return h
        #     h += 1
        # return -1


start_time = time()

# _haystack = "hello"
# _needle = "lld"
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

_haystack = "sadbutsad"
_needle = "sad"
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

print(Solution().strStr(_haystack, _needle))

print("--- %s seconds ---" % (time() - start_time))