from time import time


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ''
            n = 0
            for i in range(len(s)):
                n += int(s[i])
                if (i+1) % k == 0:
                    new_s += str(n)
                    n = 0
            if (i+1) % k != 0:
                new_s += str(n)
            s = new_s
        return s


start_time = time()

_s = "1234"
_k = 2
# Input: s = "11111222223", k = 3
# Output: "135"
# Explanation:
# - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
#   Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5.
#   So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
# - For the second round, we divide s into "346" and "5".
#   Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5.
#   So, s becomes "13" + "5" = "135" after second round.
# Now, s.length <= k, so we return "135" as the answer.

print(Solution().digitSum(_s, _k))

print("--- %s seconds ---" % (time() - start_time))
