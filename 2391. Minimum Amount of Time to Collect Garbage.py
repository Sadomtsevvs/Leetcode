from time import time
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        dist = 0
        time_to_take = 0
        m, p, g = 0, 0, 0
        for i, garb in enumerate(garbage):
            time_to_take += len(garb)
            if i > 0:
                dist += travel[i - 1]
            if 'M' in garb:
                m = dist
            if 'P' in garb:
                p = dist
            if 'G' in garb:
                g = dist
        return time_to_take + m + p + g

        # dist = 0
        # m, p, g = 0, 0, 0
        # res_m, res_p, res_g = 0, 0, 0
        # for i, garb in enumerate(garbage):
        #     cntr = Counter(garb)
        #     if i > 0:
        #         dist += travel[i-1]
        #     if cntr['M'] > 0:
        #         m += cntr['M']
        #         res_m = m + dist
        #     if cntr['P'] > 0:
        #         p += cntr['P']
        #         res_p = p + dist
        #     if cntr['G'] > 0:
        #         g += cntr['G']
        #         res_g = g + dist
        # return res_m + res_p + res_g

        # travel = [0] + travel
        # for i, g in enumerate(garbage):
        #     garbage[i] = Counter(g)
        # ans = 0
        # for t in ('M', 'P', 'G'):
        #     cur = 0
        #     for i, g in enumerate(garbage):
        #         cur += travel[i]
        #         num = g[t]
        #         cur += num
        #         if num > 0:
        #             ans += cur
        #             cur = 0
        # return ans

        # from comments
        #
        # timePicking = 0
        # timeDriving = 0
        # m,p,g = -1, -1, -1
        # for i in range(len(garbage)):
        #     timePicking += len(garbage[i])
        #     if i >0:
        #         timeDriving += travel[i-1]
        #     if "M" in garbage[i]:
        #         m = timeDriving
        #     if "P" in garbage[i]:
        #         p = timeDriving
        #     if "G" in garbage[i]:
        #         g = timeDriving
        # return timePicking + (m if m!=-1 else 0) + (p if p != -1 else 0) + (g if g!=-1 else 0)

        # great solution from editorial
        #
        # ans = []
        # for i in range(len(nums)):
        #     curr = nums[i][i]
        #     ans.append("1" if curr == "0" else "0")
        # return "".join(ans)


start_time = time()

# Example 1:
# Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
_garbage = ["G","P","GP","GG"]
_travel = [2,4,3]
# Output: 21
# Explanation:
# The paper garbage truck:
# 1. Travels from house 0 to house 1
# 2. Collects the paper garbage at house 1
# 3. Travels from house 1 to house 2
# 4. Collects the paper garbage at house 2
# Altogether, it takes 8 minutes to pick up all the paper garbage.
# The glass garbage truck:
# 1. Collects the glass garbage at house 0
# 2. Travels from house 0 to house 1
# 3. Travels from house 1 to house 2
# 4. Collects the glass garbage at house 2
# 5. Travels from house 2 to house 3
# 6. Collects the glass garbage at house 3
# Altogether, it takes 13 minutes to pick up all the glass garbage.
# Since there is no metal garbage, we do not need to consider the metal garbage truck.
# Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.
#
# Example 2:
# Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
# Output: 37
# Explanation:
# The metal garbage truck takes 7 minutes to pick up all the metal garbage.
# The paper garbage truck takes 15 minutes to pick up all the paper garbage.
# The glass garbage truck takes 15 minutes to pick up all the glass garbage.
# It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.

print(Solution().garbageCollection(_garbage, _travel))

print("--- %s seconds ---" % (time() - start_time))