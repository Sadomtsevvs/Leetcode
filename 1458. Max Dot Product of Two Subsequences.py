from functools import cache
from time import time
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        # after reading Editorial
        #
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            return max(dp(i, j + 1), dp(i + 1, j), nums1[i] * nums2[j] + dp(i + 1, j + 1))

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        if min(nums2) > 0 and max(nums1) < 0:
            return min(nums2) * max(nums1)

        return dp(0, 0)

        # my first solution
        #
        # @cache
        # def dp(i, j, take):
        #     if i == len(nums1) or j == len(nums2):
        #         return 0 if take else -10 ** 6
        #
        #     result = -10 ** 6
        #     result = max(result, dp(i + 1, j + 1, take))
        #     result = max(result, dp(i, j + 1, take))
        #     result = max(result, dp(i + 1, j, take))
        #     result = max(result, nums1[i] * nums2[j] + dp(i + 1, j + 1, True))
        #
        #     return result
        #
        # return dp(0, 0, False)

        # Lee solution
        #
        # n, m = len(A), len(B)
        # dp = [[0] * (m) for i in xrange(n)]
        # for i in xrange(n):
        #     for j in xrange(m):
        #         dp[i][j] = A[i] * B[j]
        #         if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
        #         if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
        #         if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
        # return dp[-1][-1]

start_time = time()

# Example 1:
# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
#
# Example 2:
# Input: nums1 = [3,-2], nums2 = [2,-6,7]
_nums1 = [3, -2]
_nums2 = [2, -6, 7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
#
# Example 3:
# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.

print(Solution().maxDotProduct(_nums1, _nums2))

print("--- %s seconds ---" % (time() - start_time))
