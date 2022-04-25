from time import time

# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size
# candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.
# You are also given an integer k. You should allocate piles of candies to k children such that each child gets
# the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.
# Return the maximum number of candies each child can get.


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        if k > sum(candies):
            return 0

        def number_of_piles_size_x(x: int) -> int:
            result = 0
            for candie in candies:
                result += candie // x
            return result

        left, right = 1, max(candies)
        while left <= right:
            mid = (right + left) // 2
            if number_of_piles_size_x(mid) < k:
                right = mid - 1
            else:
                left = mid + 1
        return left-1


start_time = time()

_candies = [5,8,6]
_k = 3
# Input: candies = [5,8,6], k = 3
# Output: 5
# Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1.
# We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children.
# It can be proven that each child cannot receive more than 5 candies.

print(Solution().maximumCandies(_candies, _k))

print("--- %s seconds ---" % (time() - start_time))
