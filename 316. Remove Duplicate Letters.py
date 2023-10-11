from time import time


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_indexes = {}
        for i, char in enumerate(s):
            last_indexes[char] = i
        stack = []
        instack = set()
        for i, char in enumerate(s):
            if char not in instack:
                while stack and ord(stack[-1]) > ord(char) and last_indexes[stack[-1]] > i:
                    d = stack.pop()
                    instack.remove(d)

                stack.append(char)
                instack.add(char)

        return ''.join(stack)



start_time = time()

# Example 1:
# Input: s = "bcabc"
# Output: "abc"
#
# Example 2:
# Input: s = "cbacdcbc"
_s = "cbacdcbc"
# Output: "acdb"

_s = "acbcacba"

print(Solution().removeDuplicateLetters(_s))

print("--- %s seconds ---" % (time() - start_time))
