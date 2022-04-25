from time import time


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:

        result = []

        def backtrack(cur_result, remain_str):
            if len(cur_result) == len(s):
                result.append(cur_result)
                return
            if remain_str[0].isdigit():
                backtrack(cur_result + remain_str[0], remain_str[1:])
            else:
                backtrack(cur_result + remain_str[0].upper(), remain_str[1:])
                backtrack(cur_result + remain_str[0].lower(), remain_str[1:])

        backtrack('', s)

        return result


start_time = time()

_s = "a1b2"

print(Solution().letterCasePermutation(_s))

print("--- %s seconds ---" % (time() - start_time))
