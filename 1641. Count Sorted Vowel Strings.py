from time import time


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp_u = [1] * n
        dp_o = [1] * n
        dp_i = [1] * n
        dp_e = [1] * n
        dp_a = [1] * n
        for i in range(1, n):
            dp_u[i] = dp_u[i - 1]
            dp_o[i] = dp_u[i - 1] + dp_o[i - 1]
            dp_i[i] = dp_u[i - 1] + dp_o[i - 1] + dp_i[i - 1]
            dp_e[i] = dp_u[i - 1] + dp_o[i - 1] + dp_i[i - 1] + dp_e[i - 1]
            dp_a[i] = dp_u[i - 1] + dp_o[i - 1] + dp_i[i - 1] + dp_e[i - 1] + dp_a[i - 1]
        return dp_u[-1] + dp_o[-1] + dp_i[-1] + dp_e[-1] + dp_a[-1]


start_time = time()

_n = 3
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

print(Solution().countVowelStrings(_n))

print("--- %s seconds ---" % (time() - start_time))
