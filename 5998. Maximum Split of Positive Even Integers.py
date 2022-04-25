from time import time


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        if finalSum % 2 != 0:
            return []
        find = finalSum // 2
        num = 1
        cur = 1
        count = 2
        for i in range(1, find + 1):
            if cur <= count:
                cur += 1
            else:
                cur = 2
                count += 1
                num += 1

        res = []

        # def find_split(cur, rest, remain, avialable):
        def find_split(cur, rest, remain, last):
            nonlocal res
            if rest == 0:
                res = cur
                return True
            if remain == 0:
                return False
            for num in range(last+1, find + 1):
                if num > rest:
                    break
                if find_split(cur + [num], rest - num, remain - 1, num):
                    return True
            return False

        find_split([], find, num, 0)
        return [i * 2 for i in res]

        # solution from winner
        #
        # if f % 2:
        #     return []
        # f //= 2
        # s = 0
        # c = []
        # x = 1
        # while x + s <= f:
        #     c.append(x)
        #     s += x
        #     x += 1
        # c[-1] += f - s
        # return [i * 2 for i in c]

        # solution from another winner
        # if finalSum & 1:
        #     return []
        # ret = []
        # now = 2
        # while True:
        #     if finalSum - now > now:
        #         finalSum -= now
        #         ret.append(now)
        #         now += 2
        #     else:
        #         ret.append(finalSum)
        #         break
        # return ret

start_time = time()

# _finalSum = 28
_finalSum = 3722146
# _finalSum = 6914017674
# Input: finalSum = 12
# Output: [2,4,6]
# Explanation: The following are some valid splits: (2 + 10), (2 + 4 + 6), and (4 + 8).
# (2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
# Note that [2,6,4], [6,2,4], etc. are also accepted.

print(Solution().maximumEvenSplit(_finalSum))

print("--- %s seconds ---" % (time() - start_time))
