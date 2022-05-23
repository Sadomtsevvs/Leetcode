from collections import Counter
from time import time
from typing import List
from functools import cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        n_str = [Counter(s) for s in strs]

        @cache
        def dp(i, mm, nn):
            if mm < 0 or nn < 0:
                return -float('inf')
            if mm == 0 and nn == 0:
                return 0
            if i == len(strs):
                return 0
            return max(dp(i+1, mm, nn), 1 + dp(i+1, mm - n_str[i]['0'], nn - n_str[i]['1']))

        return dp(0, m, n)

        # TLE

        # n_str = [[len(s), Counter(s)] for s in strs]
        # n_str.sort(key=lambda x: x[0])
        #
        # res = [0]
        #
        # def greedy(start_ind, remain_0, remain_1, cur_len):
        #     if remain_0 < 0 or remain_1 < 0:
        #         return 0
        #     res[0] = max(cur_len, res[0])
        #     if remain_0 == 0 and remain_1 == 0:
        #         return cur_len
        #     for i in range(start_ind, len(strs)):
        #         result = greedy(i + 1, remain_0 - n_str[i][1]['0'], remain_1 - n_str[i][1]['1'], cur_len + 1)
        #         if result == 0:
        #             continue
        #         else:
        #             return result
        #     return 0
        #
        # greedy(0, m, n, 0)
        # return res[0]



start_time = time()

_strs = ["10","0001","111001","1","0"]
_m = 5
_n = 3
# _strs = ["01","00","0","11","1"]
# _m = 2
# _n = 1
# _strs = ["10","0001","111001","1","0"]
# _m = 3
# _n = 4
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

print(Solution().findMaxForm(_strs, _m, _n))

print("--- %s seconds ---" % (time() - start_time))
