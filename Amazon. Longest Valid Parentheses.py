from time import time


class Solution:
    def get_longest_valid_parenthesis(self, string: str) -> str:
        stack = []
        max_len = 0
        beg, end = -1, -1
        for i in range(len(string)):
            if stack and string[i] == ')' and stack[-1][0] == '(':
                new_beg = stack.pop()[1]
                if not stack:
                    new_beg = 0
                elif stack[-1][1] + 1 < new_beg:
                    new_beg = stack[-1][1] + 1
                if i - new_beg > max_len:
                    beg, end = new_beg, i
                    max_len = end - beg
            else:
                stack.append((string[i], i))
        return '' if end == -1 else string[beg:end+1]


start_time = time()

_string = ')(())(((()))())))('
_string = ')(()()(()))()(((())))'
# given a string which consists of (,) characters, get the longest substring which is valid .
# valid cases are (),(()).. etc so on

print(Solution().get_longest_valid_parenthesis(_string))

print("--- %s seconds ---" % (time() - start_time))
