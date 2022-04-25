from time import time


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # this is not my idea
        ls = list(s)
        stack = []
        for i in range(len(ls)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    ls[i] = ''
        while stack:
            ls[stack.pop()] = ''
        return ''.join(ls)

        # it doesn't work, two pointers
        #
        # left = right = ''
        # l, r = 0, len(s) - 1
        # while l < r:
        #     while s[l] != "(" and s[l] != ")" and l < r:
        #         left += s[l]
        #         l += 1
        #     while s[r] != "(" and s[r] != ")" and l < r:
        #         right = s[r] + right
        #         r -= 1
        #     if s[l] == "(" and s[r] == ")" and l < r:
        #         left += s[l]
        #         l += 1
        #         right = s[r] + right
        #         r -= 1
        #     if s[l] == ")":
        #         l += 1
        #     if s[r] == "(":
        #         r -= 1
        # if l == r and s[l] != "(" and s[l] != ")":
        #     left += s[l]
        # return left + right


start_time = time()

_s = "lee(t(c)o)de)"
_s = "a)b(c)d"
_s = ")f("
_s = "())()((("
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

print(Solution().minRemoveToMakeValid(_s))

print("--- %s seconds ---" % (time() - start_time))
