from time import time
from math import log10



class Solution:
    def findNumbers(self, nums: list[int]) -> int:

        res = 0
        for i in nums:
            if i < 10:
                pass
            elif i < 100:
                res += 1
            elif i < 1000:
                pass
            elif i < 10000:
                res += 1
            elif i < 100000:
                pass
            else:
                res += 1
        return res


        """
        res = 0
        for i in nums:
            if log10(i) % 2 >= 1:
                res += 1
        return res
        """

        """
        res = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                res += 1
        return res
        """


start_time = time()

_nums = [12, 345, 2, 6, 7896]

print(Solution().findNumbers(_nums))

print("--- %s seconds ---" % (time() - start_time))
