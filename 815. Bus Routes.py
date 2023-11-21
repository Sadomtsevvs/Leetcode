from collections import defaultdict
from time import time
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        buses = defaultdict(list)
        for bus, bus_routes in enumerate(routes):
            for route in bus_routes:
                buses[route].append(bus)

        count = 0
        seen = set()
        next_buses = buses[source]
        while next_buses:
            count += 1
            for bus in next_buses:
                next_routes = set()
                if bus not in seen:
                    seen.add(bus)
                    for route in routes[bus]:
                        if route == target:
                            return count
                        next_routes.add(route)
            next_buses = {bus for route in next_routes for bus in buses[route] if bus not in seen}

        return -1


start_time = time()

_routes = [[10,13,22,28,32,35,43],[2,11,15,25,27],[6,13,18,25,42],[5,6,20,27,37,47],[7,11,19,23,35],
          [7,11,17,25,31,43,46,48],[1,4,10,16,25,26,46],[7,11],[3,9,19,20,21,24,32,45,46,49],[11,41]]
_source = 37
_target = 43

print(Solution().numBusesToDestination(_routes, _source, _target))

print("--- %s seconds ---" % (time() - start_time))
