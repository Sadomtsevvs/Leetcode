from time import time
from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def cost_to_make_goal(goal):
            res = 0
            for i, num in enumerate(nums):
                res += abs(num - goal) * cost[i]
            return res

        beg, end = min(nums), max(nums)
        ans = cost_to_make_goal(nums[0])

        while beg < end:
            mid = (beg + end) // 2
            cost_mid_1 = cost_to_make_goal(mid)
            cost_mid_2 = cost_to_make_goal(mid + 1)
            ans = min(cost_mid_1, cost_mid_2)
            if cost_mid_1 > cost_mid_2:
                beg = mid + 1
            else:
                end = mid

        return ans


start_time = time()

# Example 1:
# Input: nums = [1,3,5,2], cost = [2,3,1,14]
_nums = [1,3,5,2]
_cost = [2,3,1,14]
# Output: 8
# Explanation: We can make all the elements equal to 2 in the following way:
# - Increase the 0th element one time. The cost is 2.
# - Decrease the 1st element one time. The cost is 3.
# - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.
#
# Example 2:
# Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
_nums = [2,2,2,2,2]
_cost = [4,2,8,1,3]
# Output: 0
# Explanation: All the elements are already equal, so no operations are needed.

# Input
# [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
# [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]
# Output
# 1910084870923
# Expected
# 1907611126748

_nums = [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
_cost = [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]

print(Solution().minCost(_nums, _cost))

print("--- %s seconds ---" % (time() - start_time))
