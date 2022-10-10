import heapq
from time import time


class Solution:
    def analitics(self):

        n, k = map(int, input().split(' '))
        deadlines = []
        heapq.heapify(deadlines)
        for i in range(n):
            t, d = map(int, input().split(' '))
            heapq.heappush(deadlines, (-d, -t, i + 1))
        tasks = {i: [] for i in range(k)}
        people = [(-float('inf'), i) for i in range(k)]
        heapq.heapify(people)
        result = 'YES'
        while deadlines:
            d, t, i = heapq.heappop(deadlines)
            remain, man = heapq.heappop(people)
            remain = -remain
            if remain == float('inf'):
                remain = -d + t
            elif remain >= -t:
                remain -= -t
            else:
                result = 'NO'
                break
            tasks[man].append(i)
            heapq.heappush(people, (-remain, man))
        print(result)
        if result == 'YES':
            for i in range(k):
                print(len(tasks[i]), *tasks[i][::-1])

        # n, k = map(int, input().split(' '))
        # last_starts, durations = [], []
        # heapq.heapify(last_starts)
        # heapq.heapify(durations)
        # for i in range(n):
        #     t, d = map(int, input().split(' '))
        #     heapq.heappush(last_starts, (d-t, t, i + 1))
        #     heapq.heappush(durations, (t, d, i + 1))
        # tasks = {i: [] for i in range(k)}
        # people = [(0, i) for i in range(k)]
        # heapq.heapify(people)
        # result = 'YES'
        # seen = set()
        # while last_starts:
        #     finish, man = heapq.heappop(people)
        #     while last_starts and last_starts[0][2] in seen:
        #         heapq.heappop(last_starts)
        #     if not last_starts:
        #         break
        #     last_start = last_starts[0][0]
        #     if last_start < finish:
        #         result = 'NO'
        #         break
        #     while durations[0][2] in seen:
        #         heapq.heappop(durations)
        #     if finish + durations[0][0] <= last_start:
        #         t, _, i = heapq.heappop(durations)
        #     else:
        #         _, t, i = heapq.heappop(last_starts)
        #     seen.add(i)
        #     tasks[man].append(i)
        #     heapq.heappush(people, (finish + t, man))
        # print(result)
        # if result == 'YES':
        #     for i in range(k):
        #         print(len(tasks[i]), *tasks[i])

# import heapq
#
# n, k = map(int, input().split(' '))
# heap = []
# heapq.heapify(heap)
# for i in range(n):
#     t, d = map(int, input().split(' '))
#     heapq.heappush(heap, (d, -t, i+1))
# tasks = {i: [] for i in range(k)}
# people = [(0, i) for i in range(k)]
# heapq.heapify(people)
# time = 0
# result = 'YES'
# while result == 'YES' and heap:
#     while heap and people and people[0][0] == time:
#         d, t, i = heapq.heappop(heap)
#         if d < time - t:
#             result = 'NO'
#             break
#         finish, man = heapq.heappop(people)
#         tasks[man].append(i)
#         heapq.heappush(people, (time-t, man))
#     time = people[0][0]
# print(result)
# if result == 'YES':
# 	for i in range(k):
# 	    print(len(tasks[i]), *tasks[i])



start_time = time()

Solution().analitics()

print("--- %s seconds ---" % (time() - start_time))
