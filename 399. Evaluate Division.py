from time import time
from collections import defaultdict


# UnionFind class
class UnionFind:
    def __init__(self, equations):
        self.root = dict()
        self.rank = dict()
        for first, second in equations:
            if self.root.get(first) is None:
                self.root[first] = first
                self.rank[first] = 1
            if self.root.get(second) is None:
                self.root[second] = second
                self.rank[second] = 1
            self.union(first, second)

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
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        union = UnionFind(equations)
        for k in union.root.keys():
            union.find(k)
        relations = dict()
        groups = defaultdict(list)
        for k, v in union.root.items():
            if k == v:
                relation = dict()
                relation[k] = 1
                relations[v] = relation
            groups[v].append(k)
        for key, group in groups.items():
            while len(relations[key]) < len(group):
                for i in range(len(equations)):
                    if relations[key].get(equations[i][0]) is not None and relations[key].get(equations[i][1]) is not None:
                        continue
                    if relations[key].get(equations[i][0]) is None and relations[key].get(equations[i][1]) is None:
                        continue
                    if relations[key].get(equations[i][1]) is None:
                        relations[key][equations[i][1]] = relations[key][equations[i][0]] / values[i]
                    else:
                        relations[key][equations[i][0]] = relations[key][equations[i][1]] * values[i]
        result = []
        for first, second in queries:
            if union.root.get(first) is None or union.root.get(second) is None:
                result.append(-1)
            elif union.find(first) != union.find(second):
                result.append(-1)
            else:
                result.append(relations[union.root.get(first)][first] / relations[union.root.get(first)][second])
        return result


start_time = time()

_equations = [["a","b"],["c","d"]]
_values = [1.0,1.0]
_queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

# _equations = [["a","b"],["b","c"]]
# _values = [2.0,3.0]
# _queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

print(Solution().calcEquation(_equations, _values, _queries))

print("--- %s seconds ---" % (time() - start_time))
