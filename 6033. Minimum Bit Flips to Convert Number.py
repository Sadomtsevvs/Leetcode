from time import time


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b_start = bin(start)
        b_goal = bin(goal)
        if len(b_start) > len(b_goal):
            b_goal = b_goal[:2] + '0'*(len(b_start)-len(b_goal)) + b_goal[2:]
        elif len(b_start) < len(b_goal):
            b_start = b_start[:2] + '0' * (len(b_goal) - len(b_start)) + b_start[2:]
        result = 0
        for i in range(1, max(len(b_start), len(b_goal)) - 1):
            if b_start[-i] != b_goal[-i]:
                result += 1
        return result



start_time = time()

_start = 0
_goal = 8

# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

print(Solution().minBitFlips(_start, _goal))

print("--- %s seconds ---" % (time() - start_time))
