from collections import defaultdict
from time import time


class Solution:
    def appealSum(self, s: str) -> int:

        # my first solution
        #
        last = {}
        result = [0] * len(s)
        for i, char in enumerate(s):
            if not result:
                result[0] = 1
            elif char not in last:
                result[i] += result[i-1] + i + 1
            else:
                result[i] += result[i-1] + (i - last[char] - 1) + 1
            last[char] = i
        return sum(result)

        # after reading Lee solution
        # influence of every letter
        # last = defaultdict(lambda: -1)
        # result = 0
        # for i, char in enumerate(s):
        #     result += (i - last[char]) * (len(s) - i)
        #     last[char] = i
        # return result


start_time = time()

_s = "abbca"
# Example 1:
# Input: s = "abbca"
# Output: 28
# Explanation: The following are the substrings of "abbca":
# - Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
# - Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
# - Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
# - Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
# - Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
# The total sum is 5 + 7 + 7 + 6 + 3 = 28.
#
# _s = "code"
# Example 2:
# Input: s = "code"
# Output: 20
# Explanation: The following are the substrings of "code":
# - Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
# - Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
# - Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6.
# - Substrings of length 4: "code" has an appeal of 4. The sum is 4.
# The total sum is 4 + 6 + 6 + 4 = 20.


print(Solution().appealSum(_s))

print("--- %s seconds ---" % (time() - start_time))