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

start_time = time()

_haystack = "hello"
_needle = "lld"
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

print(Solution().strStr(_haystack, _needle))

print("--- %s seconds ---" % (time() - start_time))