import heapq
from collections import Counter
from time import time
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cur_time = 0

        cntr = Counter(tasks)

        heap = [(-v, k) for k, v in cntr.items()]
        heapq.heapify(heap)

        while heap:

            queue = []
            i = 0

            while i <= n:
                cur_time += 1
                value, task = heapq.heappop(heap)
                if value != -1:
                    queue.append((value + 1, task))
                if not heap and not queue:
                    break
                i += 1
            for value, task in queue:
                heapq.heappush(heap, (value, task))

        return cur_time

        # cur_time = 0
        #
        # cntr = Counter(tasks)
        #
        # heap = [(-v, k) for k, v in cntr.items()]
        # heapq.heapify(heap)
        #
        # queue = []
        # heapq.heapify(queue)
        #
        # while heap or queue:
        #
        #     if queue and queue[0][0] == cur_time:
        #         time, task, value = heapq.heappop(queue)
        #         value -= 1
        #         if value:
        #             heapq.heappush(queue, (cur_time + n + 1, task, value))
        #     elif heap:
        #         value, task = heapq.heappop(heap)
        #         value += 1
        #         if value:
        #             heapq.heappush(queue, (cur_time + n + 1, task, -value))
        #     else:
        #         pass
        #
        #     cur_time += 1
        #
        # return cur_time


start_time = time()

# /*
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.
#
# Example 1:
#
_tasks = ["A","A","A","B","B","B"]
_n = 2
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
#
# There is at least 2 units of time between any two same tasks.
# Example 2:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:
#
_tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
_n = 2
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

_tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
_n = 2
# Output 13
# Expected 12
# A - B - C - D - A - B - C - A - B - C - D - E


print(Solution().leastInterval(_tasks, _n))

print("--- %s seconds ---" % (time() - start_time))
