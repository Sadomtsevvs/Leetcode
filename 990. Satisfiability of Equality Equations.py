from time import time
from typing import List
from string import ascii_lowercase


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # my first solution, doesn't work
        #
        # dic = dict()
        # for a, sign, sign2, b in equations:
        #     if sign == '!':
        #         if a == b:
        #             return False
        #         if a not in dic:
        #             dic[a] = [set(b), set(a)]
        #         else:
        #             dic[a][0].add(b)
        #         if b not in dic:
        #             dic[b] = [set(a), set(b)]
        #         else:
        #             dic[b][0].add(a)
        #         for un in dic[a][1]:
        #             dic[un][0] = dic[a][0]
        #             dic[b][0].add(un)
        #         for un in dic[b][1]:
        #             dic[un][0] = dic[b][0]
        #             dic[a][0].add(un)
        #         if b in dic[a][1] or a in dic[b][1]:
        #             return False
        #     else:
        #         if a == b:
        #             continue
        #         if a not in dic:
        #             dic[a] = [set(), {a, b}]
        #         else:
        #             dic[a][1] = dic[a][1].union(dic[b][1])
        #         if b not in dic:
        #             dic[b] = [set(), {a, b}]
        #         else:
        #             dic[b][1] = dic[b][1].union(dic[a][1])
        #         for un in dic[a][1]:
        #             dic[un][1] = dic[a][1]
        #             dic[b][1].add(un)
        #         for un in dic[b][1]:
        #             dic[un][1] = dic[b][1]
        #             dic[a][1].add(un)
        #         if b in dic[a][0] or a in dic[b][0]:
        #             return False
        # return True

        # Lee solution
        #
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        uf = {a: a for a in ascii_lowercase}
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)

        # my solution after Lee
        #
        # uf = {a: a for a in ascii_lowercase}
        #
        # def union(x, y):
        #     f_x = find(x)
        #     f_y = find(y)
        #     if f_x == f_y:
        #         return
        #     if f_x < f_y:
        #         uf[f_y] = f_x
        #     else:
        #         uf[f_x] = f_y
        #
        # def find(x):
        #     if uf[x] == x:
        #         return x
        #     uf[x] = find(uf[x])
        #     return uf[x]
        #
        # for a, sign, _, b in equations:
        #     if sign == '=':
        #         union(a, b)
        #
        # for a, sign, _, b in equations:
        #     if sign == '!':
        #         if find(a) == find(b):
        #             return False
        #
        # return True


start_time = time()

_equations = ["a==b","b!=a"]
# Example 1:
# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
#
_equations = ["b==a","a==b"]
# Example 2:
# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

_s = "hdklqkcssgxlvehva" # hdklq + kcs + sgxlveh + va
# Output: 2
# Expected: 4

_equations = ["a==b","e==c","b==c","a!=e"]
_equations = ["a==b","b==c","a==c"]

print(Solution().equationsPossible(_equations))

print("--- %s seconds ---" % (time() - start_time))
