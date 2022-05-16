from time import time


class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for bracket in s:
        #     if not stack:
        #         stack.append(bracket)
        #     elif stack[-1] == "(" and bracket == ")":
        #         stack.pop()
        #     elif stack[-1] == "{" and bracket == "}":
        #         stack.pop()
        #     elif stack[-1] == "[" and bracket == "]":
        #         stack.pop()
        #     else:
        #         stack.append(bracket)
        # return not stack

        # another solution
        #
        stack = []
        for char in s:
            if stack and ((char == ")" and stack[-1] == '(') or (char == "}" and stack[-1] == '{') or (char == "]" and stack[-1] == '[')):
                stack.pop()
            else:
                stack.append(char)
        return not stack


start_time = time()

_s = "()[]{}"
_s = "((({}))[]"
_s = "]"
# Input: s = "()[]{}"
# Output: true

print(Solution().isValid(_s))

print("--- %s seconds ---" % (time() - start_time))
