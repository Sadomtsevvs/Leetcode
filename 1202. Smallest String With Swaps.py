from time import time
from collections import defaultdict


# solution from LC comments

# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        u = UnionFind(len(s))
        for i, j in pairs:
            u.union(i, j)
        d = defaultdict(list)
        for i in range(len(s)):
            d[u.find(i)].append(s[i])
        for el in d:
            d[el].sort(reverse=True)
        result = ''
        for i in range(len(s)):
            result += d[u.find(i)].pop()
        return result


start_time = time()

_s = "dcab"
_pairs = [[0,3],[1,2]]
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"

# _s = "dcab"
# _pairs = [[0,3],[1,2],[0,2]]
# # Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# # Output: "abcd"
# # Explaination:
# # Swap s[0] and s[3], s = "bcad"
# # Swap s[0] and s[2], s = "acbd"
# # Swap s[1] and s[2], s = "abcd"

print(Solution().smallestStringWithSwaps(_s, _pairs))

print("--- %s seconds ---" % (time() - start_time))
