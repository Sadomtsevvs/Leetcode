from time import time


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(acc) for acc in accounts])

        # from LC comments
        #
        # return max(map(sum, accounts))


start_time = time()

_accounts = [[1,2,3],[3,2,1]]
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

print(Solution().maximumWealth(_accounts))

print("--- %s seconds ---" % (time() - start_time))
