from functools import cache
from time import time
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        m = len(potions)
        for spell in spells:
            beg, end = 0, m - 1
            while beg <= end:
                mid = (beg + end) // 2
                if spell * potions[mid] < success:
                    beg = mid + 1
                else:
                    end = mid - 1
            result.append(0 if beg == m else m - beg)
        return result


start_time = time()


# Example 1:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
_spells = [5,1,3]
_potions = [1,2,3,4,5]
_success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
#
# Example 2:
# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
# Thus, [2,0,2] is returned.


print(Solution().successfulPairs(_spells, _potions, _success))

print("--- %s seconds ---" % (time() - start_time))
