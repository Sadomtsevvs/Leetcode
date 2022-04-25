from time import time
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # this doesn't work with input: [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        # because KUL is the last, it can't be taken in first step
        #
        # itineraries = defaultdict(list)
        # for from1, to1 in tickets:
        #     itineraries[from1].append(to1)
        # for from1 in itineraries.keys():
        #     itineraries[from1].sort(reverse=True)
        # result = ["JFK"]
        # while len(result) < len(tickets) + 1:
        #     result.append(itineraries[result[-1]].pop())
        # return result

        itineraries = defaultdict(list)

        for from1, to1 in tickets:
            itineraries[from1].append(to1)
        for from1 in itineraries.keys():
            itineraries[from1].sort(reverse=True)

        def dfs(res):
            if len(res) == len(tickets) + 1:
                return res
            for i in range(len(itineraries[res[-1]])-1, -1, -1):
                to1 = itineraries[res[-1]].pop(i)
                result = dfs(res + [to1])
                if result:
                    return result
                itineraries[res[-1]].insert(i, to1)
            return False

        return dfs(["JFK"])

        # solution from LC comments, but i don't quiet understand it
        # try to explain: we will add first the node with no way from it, i.e. last destination point
        # so, last node is "JFK"
        # answer need to be returned
        #
        # mem = defaultdict(list)
        # for t in tickets:
        #     mem[t[0]].append(t[1])
        # for i in mem.keys():
        #     mem[i].sort(reverse=True)
        #
        # ans = []
        #
        # def dfs(node):
        #     while mem[node]:
        #         i = mem[node].pop()
        #         dfs(i)
        #     ans.append(node)
        #
        # dfs("JFK")
        # return ans[::-1]

        # another solutions from comments
        #
        # def findItinerary(self, tickets):
        #     targets = collections.defaultdict(list)
        #     for a, b in sorted(tickets)[::-1]:
        #         targets[a] += b,
        #     route = []
        #
        #     def visit(airport):
        #         while targets[airport]:
        #             visit(targets[airport].pop())
        #         route.append(airport)
        #
        #     visit('JFK')
        #     return route[::-1]
        #
        # Iterative
        # version:
        #
        # def findItinerary(self, tickets):
        #     targets = collections.defaultdict(list)
        #     for a, b in sorted(tickets)[::-1]:
        #         targets[a] += b,
        #     route, stack = [], ['JFK']
        #     while stack:
        #         while targets[stack[-1]]:
        #             stack += targets[stack[-1]].pop(),
        #         route += stack.pop(),
        #     return route[::-1]


start_time = time()

_tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# _tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

print(Solution().findItinerary(_tickets))

print("--- %s seconds ---" % (time() - start_time))
