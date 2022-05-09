from time import time


class Solution:
    def isBalanced(self, s):
        stack = []
        for char in s:
            if stack and \
                    ((stack[-1] == '(' and char == ')')
                     or (stack[-1] == '[' and char == ']')
                     or (stack[-1] == '{' and char == '}')):
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


start_time = time()

_s = '{[()]}'
_s = '{(})'
# s = {[()]}
# output: true

print(Solution().isBalanced(_s))

print("--- %s seconds ---" % (time() - start_time))
