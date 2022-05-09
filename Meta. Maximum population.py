from time import time
from heapq import *
from collections import defaultdict


class Solution:
    def max_population(self, people):
        # b_heap, d_heap = [], []
        # heapify(b_heap)
        # heapify(d_heap)
        # min_period, max_period = float('inf'), -float('inf')
        # for b, d in people:
        #     heappush(b_heap, b)
        #     heappush(d_heap, d)
        #     min_period = min(min_period, b)
        #     max_period = max(max_period, d)
        # result = [0]
        # for i in range(min_period, max_period + 1):
        #     births = 0
        #     while b_heap and b_heap[0] == i:
        #         births += 1
        #         heappop(b_heap)
        #     deaths = 0
        #     while d_heap and d_heap[0] == i-1:
        #         deaths += 1
        #         heappop(d_heap)
        #     result.append(result[-1] + births - deaths)
        # max_people = 0
        # max_ind = -1
        # for i in range(len(result)):
        #     if result[i] > max_people:
        #         max_people = result[i]
        #         max_ind = i
        # return min_period + max_ind - 1, max_people

        bd_heap = []
        heapify(bd_heap)
        births_deaths = defaultdict(int)
        for b, d in people:
            births_deaths[b] += 1
            births_deaths[d + 1] -= 1
        for year, adds in births_deaths.items():
            heappush(bd_heap, (year, adds))
        max_people = 0
        cur_people = 0
        max_year = -1
        while bd_heap:
            year, adds = heappop(bd_heap)
            cur_people += adds
            if cur_people > max_people:
                max_people = cur_people
                max_year = year
        return max_year, max_people


start_time = time()

_people = [[1936, 1982], [1955, 2014], [1945, 1999], [1980, 2020], [1971, 2040], [1984, 2015], [1990, 2022]]

print(Solution().max_population(_people))

print("--- %s seconds ---" % (time() - start_time))
