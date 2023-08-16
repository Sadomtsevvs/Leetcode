from time import time
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    operand = stack.pop()
                    stack[-1] = stack[-1] + operand
                case '-':
                    operand = stack.pop()
                    stack[-1] = stack[-1] - operand
                case '*':
                    operand = stack.pop()
                    stack[-1] = stack[-1] * operand
                case '/':
                    operand = stack.pop()
                    stack[-1] = int(stack[-1] / operand)
                case _:
                    stack.append(int(token))
        return stack[0]


start_time = time()

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
_tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

print(Solution().evalRPN(_tokens))

print("--- %s seconds ---" % (time() - start_time))
