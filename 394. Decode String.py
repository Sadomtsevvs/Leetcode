from time import time


class Solution:
    def decodeString(self, s: str) -> str:

        result = ''
        stack = []
        i = 0
        while i < len(s):
            symb = s[i]
            if symb == '[':
                stack.append('')
                i += 1
            elif symb == ']':
                string, mult = stack.pop(), stack.pop()
                if not stack:
                    result += string * mult
                else:
                    stack[-1] += string * mult
                i += 1
            elif symb.isalpha():
                if not stack:
                    result += symb
                else:
                    stack[-1] += symb
                i += 1
            else:
                mult = 0
                while symb.isnumeric():
                    mult *= 10
                    mult += int(symb)
                    i += 1
                    symb = s[i]
                stack.append(mult)
        return result

        # from comments
        #
        # stack = []; curNum = 0; curString = ''
        # for c in s:
        #     if c == '[':
        #         stack.append(curString)
        #         stack.append(curNum)
        #         curString = ''
        #         curNum = 0
        #     elif c == ']':
        #         num = stack.pop()
        #         prevString = stack.pop()
        #         curString = prevString + num*curString
        #     elif c.isdigit():
        #         curNum = curNum*10 + int(c)
        #     else:
        #         curString += c
        # return curString


start_time = time()

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#
# Example 2:
# Input: s = "3[a2[c]]"
_s = "3[a2[c]]"
# Output: "accaccacc"
#
# Example 3:
# Input: s = "2[abc]3[cd]ef"
_s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

print(Solution().decodeString(_s))

print("--- %s seconds ---" % (time() - start_time))
