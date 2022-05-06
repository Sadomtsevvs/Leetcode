from time import time


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack[-1][1] == k:
                stack.pop()
        return ''.join(char * n for char, n in stack)


start_time = time()

_s = "deeedbbcccbdaa"
_k = 3
_s = "pbbcggttciiippooaais"
_k = 2
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation:
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

print(Solution().removeDuplicates(_s, _k))

print("--- %s seconds ---" % (time() - start_time))
