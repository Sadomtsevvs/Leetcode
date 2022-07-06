from time import time
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        right_candles = [0] * len(s)
        candle_idx = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '|':
                candle_idx = i
            right_candles[i] = candle_idx

        left_candles = [0] * len(s)
        candle_idx = -1
        num_candles = [0] * len(s)
        cur_candle = 0
        for i in range(len(s)):
            if s[i] == '|':
                candle_idx = i
                cur_candle += 1
            left_candles[i] = candle_idx
            num_candles[i] = cur_candle

        ans = []
        for beg, end in queries:
            right_candle = right_candles[beg]
            left_candle = left_candles[end]
            if right_candle == -1 or right_candle == -1 or right_candle >= left_candle:
                ans.append(0)
            else:
                ans.append(left_candle - right_candle - (num_candles[left_candle] - num_candles[right_candle]))
        return ans


start_time = time()

_s = "**|**|***|"
_queries = [[2,5],[5,9],[0,1]]
# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.

_s = "***|**|*****|**||**|*"
_queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Output: [9,0,0,0,0]
# Explanation:
# - queries[0] has nine plates between candles.
# - The other queries have zero plates between candles.



print(Solution().platesBetweenCandles(_s, _queries))

print("--- %s seconds ---" % (time() - start_time))