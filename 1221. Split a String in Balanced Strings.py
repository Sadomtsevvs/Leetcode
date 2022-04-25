from time import time


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        count_r, count_l = 0, 0
        for char in s:
            if char == "R":
                count_r += 1
            else:
                count_l += 1
            if count_r == count_l:
                ans += 1
        return ans


start_time = time()

_s = "RLRRLLRLRL"
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

print(Solution().balancedStringSplit(_s))

print("--- %s seconds ---" % (time() - start_time))
