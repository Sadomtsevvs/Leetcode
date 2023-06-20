from time import time
from typing import List
from bisect import bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        # official solution

        dp = {}
        arr2.sort()

        def dfs(i, prev):
            if i == len(arr1):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]

            cost = float('inf')

            # If arr1[i] is already greater than prev, we can leave it be.
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])

            # Find a replacement with the smallest value in arr2.
            idx = bisect_right(arr2, prev)

            # Replace arr1[i], with a cost of 1 operation.
            if idx < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))

            dp[(i, prev)] = cost
            return cost

        res = dfs(0, -1)

        return res if res < float('inf') else -1


start_time = time()

# Example 1:
# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
_arr1 = [1,5,3,6,7]
_arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
#
# Example 2:
# Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# Output: 2
# Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
#
# Example 3:
# Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# Output: -1
# Explanation: You can't make arr1 strictly increasing.

print(Solution().makeArrayIncreasing(_arr1, _arr2))

print("--- %s seconds ---" % (time() - start_time))
