from collections import defaultdict
from time import time
import heapq


class Solution:
    def planner(self):
        result = dict()
        queues = defaultdict(list)
        n, m, k = map(int, input().split(' '))
        for i in range(n):
            s, q, t = map(int, input().split(' '))
            queues[q].append((s, t, i + 1))
        workers = [(1, i) for i in range(1, m + 1)]
        heapq.heapify(workers)
        priorities = [(0, i, 0) for i in range(1, k + 1)]
        heapq.heapify(priorities)
        done = 0
        while done != n:
            cur_time, worker = heapq.heappop(workers)
            min_start, min_queue, min_ind = float('inf'), None, None
            temp = []
            while priorities and queues[priorities[0][1]][priorities[0][2]][0] > cur_time:
                _, queue_num, ind = heapq.heappop(priorities)
                next_start = queues[queue_num][ind][0]
                if next_start < min_start:
                    min_start = next_start
                    min_queue = queue_num
                    min_ind = ind
                temp.append((next_start, queue_num, ind))
            if priorities:
                s, t, task_num = queues[priorities[0][1]][priorities[0][2]]
                result[task_num] = (worker, cur_time)
                heapq.heappush(workers, (cur_time + t, worker))
                done += 1
                _, queue_num, ind = heapq.heappop(priorities)
                ind += 1
                if ind < len(queues[queue_num]):
                    heapq.heappush(priorities, (cur_time, queue_num, ind))
                else:
                    del queues[queue_num]
                while temp:
                    heapq.heappush(priorities, temp.pop())
            else:
                cur_time = min_start
                s, t, task_num = queues[min_queue][min_ind]
                result[task_num] = (worker, cur_time)
                heapq.heappush(workers, (cur_time + t, worker))
                done += 1
                min_ind += 1
                if min_ind < len(queues[min_queue]):
                    heapq.heappush(priorities, (cur_time, min_queue, min_ind))
                else:
                    del queues[min_queue]
                while temp:
                    if temp[-1][1] == min_queue:
                        temp.pop()
                    else:
                        heapq.heappush(priorities, temp.pop())
        for i in range(1, n+1):
            print(*result[i])


start_time = time()

Solution().planner()

print("--- %s seconds ---" % (time() - start_time))
