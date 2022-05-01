from time import time
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        last_positions = dict()
        for i in range(len(cards)):
            card = cards[i]
            if last_positions.get(card) is None:
                last_positions[card] = i
            else:
                dist = i - last_positions[card] + 1
                ans = min(ans, dist)
                last_positions[card] = i
        return -1 if ans == float('inf') else ans


start_time = time()

_cards = [3,4,2,3,4,7]
# Input: cards = [3,4,2,3,4,7]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3.
# Note that picking up the cards [4,2,3,4] is also optimal.

print(Solution().minimumCardPickup(_cards))

print("--- %s seconds ---" % (time() - start_time))
