from time import time


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
            return res if res < 2**31 - 1 else 0
        res = int('-' + str(x)[1:][::-1])
        return res if res > -2**31 else 0


start_time = time()

data = -123
print(Solution().reverse(data))

print("--- %s seconds ---" % (time() - start_time))