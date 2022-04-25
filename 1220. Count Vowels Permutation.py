from time import time
from functools import lru_cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:

        # recursion, too slow
        #
        # result = 0
        # allowed = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        #
        # def add_vowel(remain, last):
        #     nonlocal result
        #     if remain == 0:
        #         result += 1
        #         return
        #     for a_vowel in allowed[last]:
        #         add_vowel(remain - 1, a_vowel)
        #
        # for vowel in allowed.keys():
        #     add_vowel(n-1, vowel)
        #
        # return result

        # allowed = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}

        def count_words(remain, last_a=0, last_e=0, last_i=0, last_o=0, last_u=0):
            if remain == 0:
                return last_a + last_e + last_i + last_o + last_u
            return count_words(remain - 1, last_e + last_i + last_u, last_a + last_i, last_e + last_o, last_i, last_i + last_o)

        result = 0
        result += count_words(n - 1, 1)
        result += count_words(n - 1, 0, 1)
        result += count_words(n - 1, 0, 0, 1)
        result += count_words(n - 1, 0, 0, 0, 1)
        result += count_words(n - 1, 0, 0, 0, 0, 1)

        return result % (10**9 + 7)

        # amazing solution from LC comments
        #
        # a, e, i, o, u = 1, 1, 1, 1, 1
        # for _ in range(n - 1):
        #     a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        # return (a + e + i + o + u) % (10**9 + 7)


start_time = time()

_n = 2000
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.

print(Solution().countVowelPermutation(_n))

print("--- %s seconds ---" % (time() - start_time))
