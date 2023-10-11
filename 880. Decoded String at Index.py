from time import time


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        stack = []
        cur_len = 0
        for i, char in enumerate(s):
            if char.isnumeric():
                stack.append(char)
                cur_len *= int(char)
                if cur_len >= k:
                    break
            else:
                if not stack or stack[-1].isnumeric():
                    stack.append(char)
                else:
                    stack[-1] += char
                cur_len += 1
                if cur_len == k:
                    return char
        while stack:
            char = stack.pop()
            if char.isnumeric():
                cur_len = cur_len // int(char)
                if cur_len == 1:
                    k = 1
                else:
                    k %= cur_len
                    if k == 0:
                        k = cur_len
            else:
                if cur_len - len(char) >= k:
                    cur_len -= len(char)
                else:
                    return char[k - (cur_len - len(char)) - 1]

        # MLE
        #
        # cur = ''
        # prev_is_numeric = False
        # for char in s:
        #     if char.isnumeric():
        #         cur = cur * int(char)
        #         prev_is_numeric = True
        #     else:
        #         if prev_is_numeric:
        #             prev_is_numeric = False
        #         cur += char
        #     if len(cur) >= k:
        #         return cur[k-1]

        # Lee solution
        #
        # N = 0
        # for i, c in enumerate(S):
        #     N = N * int(c) if c.isdigit() else N + 1
        #     if K <= N: break
        # for j in range(i, -1, -1):
        #     c = S[j]
        #     if c.isdigit():
        #         N /= int(c)
        #         K %= N
        #     else:
        #         if K == N or K == 0: return c
        #         N -= 1


start_time = time()

# Example 1:
# Input: s = "leet2code3", k = 10
_s = "leet2code3"
_k = 10
# Output: "o"
# Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o"
#
# Example 2:
# Input: s = "ha22", k = 5
_s = "ha22"
_k = 3
# Output: "h"
# Explanation: The decoded string is "hahahaha".
# The 5th letter is "h".
#
# Example 3:
# Input: s = "a2345678999999999999999", k = 1
# Output: "a"
# Explanation: The decoded string is "a" repeated 8301530446056247680 times.
# The 1st letter is "a".

_s = "a2b3c4d5e6f7g8h9"
_k = 4
# Output
# "c"
# Expected
# "b"

# _s = "cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg"
# _k = 480551547

_s = "vk6u5xhq9v"
_k = 554

# Use Testcase
# Output
# "v"
# Expected
# "k"

print(Solution().decodeAtIndex(_s, _k))

print("--- %s seconds ---" % (time() - start_time))
