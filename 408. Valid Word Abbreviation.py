from time import time


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        coeffs = []
        cur = 0
        for a in abbr:
            if a.isdigit():
                cur = cur * 10 + int(a)
            else:
                if cur != 0:
                    coeffs.append(cur)
                    cur = 0
                coeffs.append(a)
        if cur != 0:
            coeffs.append(cur)
        w = 0
        for a in coeffs:
            if w >= len(word):
                return False
            if isinstance(a, int):
                w += a
            elif a == word[w]:
                w += 1
            else:
                return False
        return True


start_time = time()

# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
_s = "internationalization"
_abbr = "i12iz4n"
# Return true.
#
# Example 2:
# Given s = "apple", abbr = "a2e":
# _s = "apple"
# _abbr = "a2e"
# Return false.

print(Solution().validWordAbbreviation(_s, _abbr))

print("--- %s seconds ---" % (time() - start_time))