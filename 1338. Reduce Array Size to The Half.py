from time import time
from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        values = list(Counter(arr).values())
        values.sort(reverse=True)
        i = 0
        deleted = 0
        while deleted < len(arr)/2:
            deleted += values[i]
            i += 1
        return i


start_time = time()

_arr = [3,3,3,3,5,5,5,2,2,7]
# Example 1:
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
#
_arr = [7,7,7,7,7,7]
# Example 2:
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.

print(Solution().minSetSize(_arr))

print("--- %s seconds ---" % (time() - start_time))
