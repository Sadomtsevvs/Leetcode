from functools import cache
from time import time
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        # my first solution, DP, O(n**2)
        #
        # satisfaction.sort()
        #
        # @cache
        # def dp(i, time):
        #     if i == len(satisfaction):
        #         return 0
        #     return max(dp(i+1, time), dp(i+1, time+1) + satisfaction[i]*time)
        #
        # return dp(0, 1)

        # after reading official greedy solution
        #
        satisfaction.sort()

        ans, cur_sfx = 0, 0
        for i in range(len(satisfaction)-1, -1, -1):
            cur_sfx += satisfaction[i]
            if cur_sfx <= 0:
                break
            ans += cur_sfx
        return ans


start_time = time()


# Example 1:
_satisfaction = [-1,-8,0,5,-9]
# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14
# Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.
#
# Example 2:
# Input: satisfaction = [4,3,2]
# Output: 20
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
#
# Example 3:
# Input: satisfaction = [-1,-4,-5]
# Output: 0
# Explanation: People do not like the dishes. No dish is prepared.


print(Solution().maxSatisfaction(_satisfaction))

print("--- %s seconds ---" % (time() - start_time))
