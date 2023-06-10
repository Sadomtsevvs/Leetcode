from time import time
from typing import List


class UnionFind:
    def __init__(self, n):
        self.distinct = n
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def connect(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 0
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        self.distinct -= 1
        return 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        uf = UnionFind(len(nums))
        skip = set()
        for i in range(len(nums)-1):
            if i in skip:
                continue
            num1 = nums[i]
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                if gcd(num1, num2) > 1:
                    uf.connect(i, j)
                    skip.add(j)
                    if uf.distinct == 1:
                        return True
        return uf.distinct == 1


start_time = time()


# Example 1:
# Input: nums = [2,3,6]
_nums = [2,3,6]
# Output: true
# Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
# To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
# To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
#
# Example 2:
# Input: nums = [3,9,5]
_nums = [3,9,5]
# Output: false
# Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
#
# Example 3:
# Input: nums = [4,3,12,8]
# _nums = [4,3,12,8]
# Output: true
# Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.

_nums = [21,21,35,20]

print(Solution().canTraverseAllPairs(_nums))

print("--- %s seconds ---" % (time() - start_time))
