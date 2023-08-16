from collections import defaultdict
from time import time
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        subs = defaultdict(int)
        for num in arr:
            prev = num - difference
            subs[num] = subs[prev] + 1
        return max(subs.values())


start_time = time()

# Example 1:
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
#
# Example 2:
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.
#
# Example 3:
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
_arr = [1,5,7,8,5,3,4,2,1]
_difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].

print(Solution().longestSubsequence(_arr, _difference))

print("--- %s seconds ---" % (time() - start_time))
