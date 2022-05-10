from time import time
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []

        def get_combs(cur_digits, next_digit):
            cur_sum = sum(cur_digits)
            if cur_sum > n or len(cur_digits) > k:
                return
            if cur_sum == n and len(cur_digits) == k:
                result.append(cur_digits)
                return
            for num in range(next_digit, 10):
                if cur_sum + num > n:
                    break
                get_combs(cur_digits + [num], num + 1)

        get_combs([], 1)
        return result


start_time = time()

_k = 3
_n = 9
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.

print(Solution().combinationSum3(_k, _n))

print("--- %s seconds ---" % (time() - start_time))
