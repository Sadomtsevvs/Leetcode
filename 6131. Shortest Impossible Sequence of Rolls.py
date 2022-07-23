from time import time
from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans = 1
        while True:
            dicts = dict()
            shortest = float('inf')
            get_nums = set()
            for i in range(len(rolls)):
                if rolls[i] not in dicts:
                    get_nums.add(rolls[i])
                    dicts[rolls[i]] = rolls[i+1:]
                    if len(dicts[rolls[i]]) < shortest:
                        shortest = len(dicts[rolls[i]])
                        best = rolls[i]
                if len(get_nums) == k:
                    break
            for i in range(1, k + 1):
                if i not in get_nums:
                    return ans
            ans += 1
            rolls = dicts[best]


start_time = time()

_rolls = [4,2,1,2,3,3,2,4,1]
_k = 4

# Example 1:
# Input: rolls = [4,2,1,2,3,3,2,4,1], k = 4
# Output: 3
# Explanation: Every sequence of rolls of length 1, [1], [2], [3], [4], can be taken from rolls.
# Every sequence of rolls of length 2, [1, 1], [1, 2], ..., [4, 4], can be taken from rolls.
# The sequence [1, 4, 2] cannot be taken from rolls, so we return 3.
# Note that there are other sequences that cannot be taken from rolls.

# _rolls = [1,1,2,2]
# _k = 2
# Example 2:
# Input: rolls = [1,1,2,2], k = 2
# Output: 2
# Explanation: Every sequence of rolls of length 1, [1], [2], can be taken from rolls.
# The sequence [2, 1] cannot be taken from rolls, so we return 2.
# Note that there are other sequences that cannot be taken from rolls but [2, 1] is the shortest.

# _rolls = [1,1,3,2,2,2,3,3]
# _k = 4
# Example 3:
# Input: rolls = [1,1,3,2,2,2,3,3], k = 4
# Output: 1
# Explanation: The sequence [4] cannot be taken from rolls, so we return 1.
# Note that there are other sequences that cannot be taken from rolls but [4] is the shortest.

print(Solution().shortestSequence(_rolls, _k))

print("--- %s seconds ---" % (time() - start_time))
