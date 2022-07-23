from collections import Counter
from time import time
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        if len(set(ranks)) == 5:
            return 'High Card'
        if len(set(ranks)) == 2:
            return 'Three of a Kind'
        for col in Counter(ranks).values():
            if col >= 3:
                return 'Three of a Kind'
        return 'Pair'


start_time = time()

_ranks = [4,4,2,4,4]
_suits = ["d","a","a","b","c"]
# Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
# Output: "Three of a Kind"
# Explanation: The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a "Three of a Kind".
# Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
# Also note that other cards could be used to make the "Three of a Kind" hand.

print(Solution().bestHand(_ranks, _suits))

print("--- %s seconds ---" % (time() - start_time))
