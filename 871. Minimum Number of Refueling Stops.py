from heapq import heappop, heappush
from time import time
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # solution after reading officical
        #
        ans = 0
        heap = []
        prev_pos = 0
        tank = startFuel
        stations.append([target, 0])
        for pos, fuel in stations:
            tank -= pos - prev_pos
            while heap and tank < 0:
                tank += -heappop(heap)
                ans += 1
            if tank < 0:
                return -1
            heappush(heap, -fuel)
            prev_pos = pos
        return ans

        # doesn't work correct
        # stations.sort(key=lambda x: (x[0], -x[1]))
        # dist = [0]
        # fuel = [startFuel]
        # prev_d = 0
        # for d, f in stations:
        #     if d == prev_d:
        #         continue
        #     dist.append(d)
        #     fuel.append(f)
        #     prev_d = d
        # dist.append(target)
        # fuel.append(0)
        # dp = [0] * len(dist)
        # for i in range(1, len(dp)):
        #     res = float('inf')
        #     idx = None
        #     for j in range(i-1, -1, -1):
        #         if dist[i] - dist[j] <= fuel[j]:
        #             prev_dp = dp[j] if j == 0 else dp[j] + 1
        #             if prev_dp < res:
        #                 res = prev_dp
        #                 idx = j
        #             # res = min(res, dp[j] if j == 0 else dp[j] + 1)
        #         # else:
        #         #     break
        #     if res == float('inf'):
        #         return -1
        #     fuel[i] += fuel[idx] - (dist[i] - dist[idx])
        #     dp[i] = res
        # return dp[-1]




start_time = time()


# Example 1:
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
#
_target = 100
_startFuel = 1
_stations = [[10,100]]
# Example 2:
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can not reach the target (or even the first gas station).
#
# _target = 100
# _startFuel = 10
# _stations = [[10,60],[20,30],[30,30],[60,40]]
# Example 3:
# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.

_target = 100
_startFuel = 50
_stations = [[40,50]]

_target = 100
_startFuel = 25
_stations = [[25,25],[50,25],[75,25]]

print(Solution().minRefuelStops(_target, _startFuel, _stations))

print("--- %s seconds ---" % (time() - start_time))
