from time import time


class Solution:
    def getBillionUsersDay(self, growthRates):
        left, right = 1, 2200
        while left < right:
            mid = (left + right) // 2
            revenue = sum(g**mid for g in growthRates)
            if revenue < 10**9:
                left = mid + 1
            else:
                right = mid
        return left


start_time = time()

_growthRates = [1.1, 1.2, 1.3]
# growthRates = [1.1, 1.2, 1.3]
# output = 79

print(Solution().getBillionUsersDay(_growthRates))

print("--- %s seconds ---" % (time() - start_time))
