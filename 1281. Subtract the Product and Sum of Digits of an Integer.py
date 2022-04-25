from time import time


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sm = 0
        for d in str(n):
            prod *= int(d)
            sm += int(d)
        return prod - sm

        # LC comments

        # a = [int(x) for x in str(n)]
        # return np.prod(a) - np.sum(a)

        # LC comments

        # A = map(int, str(n))
        # return reduce(operator.mul, A) - sum(A)

        # LC comments

        # my_prod, my_sum = 1, 0
        # while n:
        #     n, remainder = divmod(n, 10)
        #     my_prod *= remainder
        #     my_sum += remainder
        # return my_prod - my_sum

start_time = time()

_n = 234
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15

print(Solution().subtractProductAndSum(_n))

print("--- %s seconds ---" % (time() - start_time))
