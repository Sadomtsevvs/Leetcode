from time import time
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # official solution
        #
        arr.sort()
        res = [1 for _ in range(len(arr))]
        idx = {v: i for i, v in enumerate(arr)}
        for i, v in enumerate(arr):
            for j in range(i):
                if v % arr[j] == 0:
                    x = v // arr[j]
                    if x in idx:
                        res[i] += res[j] * res[idx[x]]
                        res[i] %= (10 ** 9 + 7)
        return sum(res) % (10 ** 9 + 7)

        # Lee solution
        #
        # dp = {}
        # for a in sorted(A):
        #     dp[a] = sum(dp[b] * dp.get(a / b, 0) for b in dp if a % b == 0) + 1
        # return sum(dp.values()) % (10**9 + 7)


start_time = time()

# Example 1:
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
#
_arr = [2,4,5,10]
# Example 2:
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

print(Solution().numFactoredBinaryTrees(_arr))

print("--- %s seconds ---" % (time() - start_time))
