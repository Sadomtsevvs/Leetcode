from time import time


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 == str2:
            return str1
        elif len(str1) == len(str2):
            return ""

        if len(str1) < len(str2):
            for i in range(len(str1), 0, -1):
                # check if div acceptable for str1
                if len(str1) % i != 0:
                    continue

                div = str1[:i]

                k = len(str1) // i
                if div * k != str1:
                    continue

                s = div * (len(str2) // len(div))

                if s == str2:
                    return div

        else:
            for i in range(len(str2), 0, -1):
                # check if div acceptable for str1
                if len(str2) % i != 0:
                    continue

                div = str2[:i]

                k = len(str2) // i
                if div * k != str2:
                    continue

                s = div * (len(str1) // len(div))

                if s == str1:
                    return div

        return ""

        # from LC comments
        #
        # s1, s2 = str1, str2
        # while s2:
        #     s1, s2 = s2, s1[:len(s1) % len(s2)]
        #
        # if s1 * (len(str1) // len(s1)) == str1 and s1 * (len(str2) // len(s1)) == str2:
        #     return s1
        # return ""

        # from LC comments
        #
        # return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ''

start_time = time()

_str1 = "ABABAB"
_str2 = "ABAB"
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

print(Solution().gcdOfStrings(_str1, _str2))

print("--- %s seconds ---" % (time() - start_time))
