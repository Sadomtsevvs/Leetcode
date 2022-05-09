from time import time
from bisect import bisect_left


class Solution:
    def getMilestoneDays(self, revenues, milestones):
        s = 0
        for i in range(len(revenues)):
            revenues[i] += s
            s = revenues[i]
        ans = []
        for milestone in milestones:
            if revenues[-1] < milestone:
                ind = -1
            else:
                ind = bisect_left(revenues, milestone) + 1
            ans.append(ind)
        return ans


start_time = time()

_revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
_milestones = [5, 100, 200, 500, 551]
# _revenues = [700, 800, 600, 400, 600, 700]
# _milestones = [3100, 2200, 800, 2100, 1000]
# _revenues = [100, 200, 300, 400, 500]
# _milestones = [300, 800, 1000, 1400]
# revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# milestones = [100, 200, 500]
# output = [4, 6, 10]

print(Solution().getMilestoneDays(_revenues, _milestones))

print("--- %s seconds ---" % (time() - start_time))
