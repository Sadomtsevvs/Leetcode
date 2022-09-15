from time import time
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        left, right = 0, len(tokens) - 1
        while left <= right:
            left_token = tokens[left]
            if power >= left_token:
                power -= left_token
                score += 1
                left += 1
            elif score > 0 and left != right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return score


start_time = time()


# Example 1:
# Input: tokens = [100], power = 50
# Output: 0
# Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.
#
# Example 2:
# Input: tokens = [100,200], power = 150
# Output: 1
# Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
# There is no need to play the 1st token since you cannot play it face up to add to your score.
#
_tokens = [100,200,300,400]
_power = 200
# Example 3:
# Input: tokens = [100,200,300,400], power = 200
# Output: 2
# Explanation: Play the tokens in this order to get a score of 2:
# 1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
# 2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
# 3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
# 4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.

_s = "hdklqkcssgxlvehva" # hdklq + kcs + sgxlveh + va
# Output: 2
# Expected: 4

print(Solution().bagOfTokensScore(_tokens, _power))

print("--- %s seconds ---" % (time() - start_time))
