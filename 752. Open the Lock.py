from time import time
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen = set('0000')
        queue = ['0000']
        turns = 0
        while queue:
            next_queue = []
            for comb in queue:
                if comb in deadends:
                    continue
                if comb == target:
                    return turns
                for i in range(4):
                    digit = int(comb[i])
                    next_digit_up = digit + 1
                    next_digit_down = digit - 1
                    if next_digit_up > 9:
                        next_digit_up = 0
                    elif next_digit_down < 0:
                        next_digit_down = 9
                    left, right = comb[:i], comb[i+1:]
                    next_comb_up = left + str(next_digit_up) + right
                    next_comb_down = left + str(next_digit_down) + right
                    if next_comb_up not in seen:
                        seen.add(next_comb_up)
                        next_queue.append(next_comb_up)
                    if next_comb_down not in seen:
                        seen.add(next_comb_down)
                        next_queue.append(next_comb_down)
            turns += 1
            queue = next_queue
        return -1


start_time = time()

# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
_deadends = ["0201","0101","0102","1212","2002"]
_target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
#
# Example 2:
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
#
# Example 3:
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.

print(Solution().openLock(_deadends, _target))

print("--- %s seconds ---" % (time() - start_time))
