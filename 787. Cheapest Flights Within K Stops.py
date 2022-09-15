from collections import defaultdict
from time import time
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        routes = defaultdict(list)
        for frm, to, price in flights:
            routes[frm].append((to, price))
        cities = [(src, 0)]
        dest_prices = defaultdict(int)
        dest_prices[src] = 0
        while k >= 0:
            k -= 1
            next_cities = []
            for city, price in cities:
                for next_city, next_price in routes[city]:
                    if next_city not in dest_prices or dest_prices[next_city] > price + next_price:
                        next_cities.append((next_city, price + next_price))
                        dest_prices[next_city] = price + next_price
            cities = next_cities
        if dst in dest_prices:
            return dest_prices[dst]
        return -1


start_time = time()

_n = 4
_flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
_src = 0
_dst = 3
_k = 1
# Example 1:
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# 
# Example 2:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# 
# Example 3:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

print(Solution().findCheapestPrice(_n, _flights, _src, _dst, _k))

print("--- %s seconds ---" % (time() - start_time))
