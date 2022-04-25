from time import time


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

        # from LC comments
        #
        # return ''.join(chr(ord(ch) + 32 * ('A' <= ch <= 'Z')) for ch in s)

start_time = time()

_s = "Hello"
# Input: s = "Hello"
# Output: "hello"

print(Solution().toLowerCase(_s))

print("--- %s seconds ---" % (time() - start_time))
