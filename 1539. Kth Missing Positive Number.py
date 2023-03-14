from time import time
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set_arr = set(arr)
        missed = 0
        num = 0
        while missed < k:
            num += 1
            if num not in set_arr:
                missed += 1
        return num

        # solution from Babichev, O(log(n)
        #
        # beg, end = 0, len(arr)
        # while beg < end:
        #     mid = (beg + end) // 2
        #     if arr[mid] - mid - 1 < k:
        #         beg = mid + 1
        #     else:
        #         end = mid
        # return end + k


start_time = time()

_arr = [2,3,4,7,11]
_k = 5
# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
#
# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


print(Solution().findKthPositive(_arr, _k))

print("--- %s seconds ---" % (time() - start_time))
