from bisect import bisect_left
from functools import cache
from time import time
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort(key=lambda x: x[0])

        @cache
        def dp(cur_time, last_event, events_left):
            if events_left == 0:
                return 0
            if last_event == len(events) - 1:
                return 0
            closest_event_ind = bisect_left(events, [cur_time, 0, 0], lo=last_event + 1)
            if closest_event_ind == len(events):
                return 0
            closest_event = events[closest_event_ind]
            take_event = dp(closest_event[1] + 1, closest_event_ind, events_left - 1) + closest_event[2]
            not_take_event = dp(cur_time, closest_event_ind, events_left)
            return max(take_event, not_take_event)

        return dp(0, -1, k)


start_time = time()

# Example 1:
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
_events = [[1,2,4],[3,4,3],[2,3,1]]
_k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
#
# Example 2:
# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
_events = [[1,2,4],[3,4,3],[2,3,10]]
_k = 2
# Output: 10
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
#
# Example 3:
# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
_events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
_k = 3
# Output: 9
# Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.

print(Solution().maxValue(_events, _k))

print("--- %s seconds ---" % (time() - start_time))
