from time import time
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        # my solution
        #
        result = []

        def dfs(cur, prev, remain):
            if remain == 0:
                result.append(cur)
                return
            for num in (prev - k, prev + k):
                if num < 0 or num > 9:
                    continue
                dfs(cur * 10 + num, num, remain - 1)
                if k == 0:
                    break

        for num in range(1, 10):
            dfs(num, num, n - 1)

        return result

        # from LC comments
        #
        # if n == 1:
        #     return [i for i in range(10)]
        #
        # # initialize the queue with candidates for the first level
        # queue = [digit for digit in range(1, 10)]
        #
        # for level in range(n-1):
        #     next_queue = []
        #     for num in queue:
        #         tail_digit = num % 10
        #         # using set() to avoid duplicates when K == 0
        #         next_digits = set([tail_digit + k, tail_digit - k])
        #
        #         for next_digit in next_digits:
        #             if 0 <= next_digit < 10:
        #                 new_num = num * 10 + next_digit
        #                 next_queue.append(new_num)
        #     # start the next level
        #     queue = next_queue
        #
        # return queue

start_time = time()

_n = 3
_k = 7
# Example 1:
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
#
# Example 2:
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

print(Solution().numsSameConsecDiff(_n, _k))

print("--- %s seconds ---" % (time() - start_time))
