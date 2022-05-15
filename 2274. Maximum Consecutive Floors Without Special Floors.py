from time import time
from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.append(bottom - 1)
        special.append(top + 1)
        special.sort()
        result = 0
        for i in range(len(special) - 1):
            result = max(result, special[i+1] - special[i] - 1)
        return result


start_time = time()

_bottom = 2
_top = 9
_special = [4,6]
# Input: bottom = 2, top = 9, special = [4,6]
# Output: 3
# Explanation: The following are the ranges (inclusive) of consecutive floors without a special floor:
# - (2, 3) with a total amount of 2 floors.
# - (5, 5) with a total amount of 1 floor.
# - (7, 9) with a total amount of 3 floors.
# Therefore, we return the maximum number which is 3 floors.

print(Solution().maxConsecutive(_bottom, _top, _special))

print("--- %s seconds ---" % (time() - start_time))