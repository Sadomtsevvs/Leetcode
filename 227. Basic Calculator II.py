from time import time


class Solution:
    def calculate(self, s: str) -> int:

        # my third solution. idea is to store the previous sign
        # 7 - 5 - 6 * 3 / 2 + 2
        result = 0
        prev_number = 0
        cur_number = 0
        signs = {'+', '-', '*', '/'}
        sign = '+'
        for i, cur_char in enumerate(s):
            if cur_char.isdigit():
                cur_number = cur_number * 10 + int(cur_char)
            if cur_char in signs or i == len(s) - 1:
                if sign == '+' or sign == '-':
                    result += prev_number
                    prev_number = cur_number if sign == '+' else -cur_number
                elif sign == '*':
                    prev_number *= cur_number
                elif sign == '/':
                    if prev_number >= 0:
                        prev_number //= cur_number
                    else:
                        prev_number = prev_number // cur_number + (1 if prev_number % cur_number > 0 else 0)
                cur_number = 0
                sign = cur_char
        return result + prev_number

        # my second solution, after reading official solution
        #
        # result = 0
        # prev_number = 0
        # cur_number = 0
        # sign = 1
        # mul_div = ''
        # for char in s:
        #     if char.isdigit():
        #         cur_number = cur_number * 10 + int(char)
        #     elif char == '+' or char == '-':
        #         if mul_div == '*':
        #             cur_number = prev_number * cur_number
        #         elif mul_div == '/':
        #             cur_number = prev_number // cur_number
        #         result += cur_number * sign
        #         cur_number = 0
        #         sign = 1 if char == '+' else -1
        #         mul_div = ''
        #     elif char == '*' or char == '/':
        #         if mul_div == '*':
        #             prev_number *= cur_number
        #         elif mul_div == '/':
        #             prev_number //= cur_number
        #         else:
        #             prev_number = cur_number
        #         cur_number = 0
        #         mul_div = char
        # if mul_div == '*':
        #     cur_number = prev_number * cur_number
        # elif mul_div == '/':
        #     cur_number = prev_number // cur_number
        # result += cur_number * sign
        # return result

        # my first solution, correct, but too long and complex
        #
        # s1 = []
        # # make * and / first:
        # operator = ''
        # length = 0
        # for char in s:
        #     if char.isdigit():
        #         if length == 0:
        #             s1.append(int(char))
        #         else:
        #             s1[-1] = s1[-1]*10 + int(char)
        #         length += 1
        #     elif char == '-' or char == '+':
        #         length = 0
        #         if operator == '*':
        #             s1[-2] *= s1[-1]
        #             s1.pop()
        #             operator = ''
        #         elif operator == '/':
        #             s1[-2] //= s1[-1]
        #             s1.pop()
        #             operator = ''
        #         s1.append(char)
        #     elif char == '*' or char == '/':
        #         length = 0
        #         if operator == '*':
        #             s1[-2] *= s1[-1]
        #             s1.pop()
        #         elif operator == '/':
        #             s1[-2] //= s1[-1]
        #             s1.pop()
        #         operator = char
        # if operator == '*':
        #     s1[-2] *= s1[-1]
        #     s1.pop()
        # elif operator == '/':
        #     s1[-2] //= s1[-1]
        #     s1.pop()
        # result = s1[0]
        # for i in range(1, len(s1)-1, 2):
        #     symb = s1[i]
        #     if symb == '+':
        #         result += s1[i+1]
        #     elif symb == '-':
        #         result -= s1[i+1]
        # return result


start_time = time()

# Example 1:
# Input: s = "3+2*2"
_s = "3+2*10"
# Output: 23
#
# Example 2:
# Input: s = " 3/2 "
# Output: 1
#
# Example 3:
# Input: s = " 3+5 / 2 "
# _s = " 3+5 / 2 "
# Output: 5

_s = "14-3/2"

print(Solution().calculate(_s))

print("--- %s seconds ---" % (time() - start_time))