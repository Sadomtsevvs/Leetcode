from time import time
from typing import List
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # solution from LC
        #
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)

        # envelopes.sort()
        # candidates = dict()
        # for w, h in envelopes:
        #     updated, maxlen = [], 0
        #     heapq.heapify(updated)
        #     for cand in candidates:
        #         cand_w, cand_h, length = candidates[cand]
        #         if cand_w < w and cand_h < h:
        #             candidates[cand] = w, h, length + 1
        #             heapq.heappush(updated, (length + 1, cand))
        #             maxlen = max(maxlen, length + 1)
        #     if not updated:
        #         candidates[(w, h)] = w, h, 1
        #     else:
        #         while len(updated) > 1:
        #             candidates.pop(heapq.heappop(updated)[1])
        # return max(v[2] for v in candidates.values())


start_time = time()

_envelopes = [[5,4],[6,4],[6,7],[2,3]]
_envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,1]]
_envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
# _envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360]]
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

print(Solution().maxEnvelopes(_envelopes))

print("--- %s seconds ---" % (time() - start_time))
