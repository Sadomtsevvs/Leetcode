from functools import cache
from time import time
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:

        # TLE

        # ans = [0]

        @cache
        def dfs(prev, rest):
            if not rest:
                return 1
            ss = set(rest)
            local_ans = 0
            for r in ss:
                if prev % r == 0 or r % prev == 0:
                    lst1 = list(ss - {r})
                    lst1.sort()
                    local_ans += dfs(r, tuple(lst1))
            return local_ans

        ans = 0
        nums = set(nums)
        for num in nums:
            lst = list(nums - {num})
            lst.sort()
            ans += dfs(num, tuple(lst))

        return ans % (10**9 + 7)

        # from LC comments
        #
        # @cache
        # def dp(i, t):
        #     if i == len(cost): return 0 if t >= 0 else inf
        #     return min(dp(i + 1, t - 1), cost[i] + dp(i + 1, min(t + time[i], len(cost))))
        #
        # return dp(0, 0)


start_time = time()

# Example 1:
# Input: nums = [2,3,6]
_nums = [2,3,6]
# Output: 2
# Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
#
# Example 2:
# Input: nums = [1,4,3]
# _nums = [1,4,3]
# Output: 2
# Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.

# Input: [20,100,50,5,10,70,7]
_nums = [20,100,50,5,10,70,7]
# Output: 6
# Expected: 48

print(Solution().specialPerm(_nums))

print("--- %s seconds ---" % (time() - start_time))
