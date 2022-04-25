from time import time


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        result = []

        if not digits:
            return result

        def bt(cur):
            if len(cur) == len(digits):
                result.append(cur)
                return
            for char in phone[digits[len(cur)]]:
                bt(cur + char)

        bt('')

        return result


start_time = time()

_digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(Solution().letterCombinations(_digits))

print("--- %s seconds ---" % (time() - start_time))
