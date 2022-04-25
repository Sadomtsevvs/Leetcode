from time import time


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in bin(n):
            if i == '1':
                res += 1
        return res

        # LC 1
        #
        # return bin(n).count('1')

        # LC 2
        #
        # counter = 0
        # while n:
        #      # this will take out the right-most 1 of n
        #      n = n & (n - 1)
        #      counter += 1
        # return counter


start_time = time()

_n = 0b0000000000000000000000000001011

print(Solution().hammingWeight(_n))

print("--- %s seconds ---" % (time() - start_time))
