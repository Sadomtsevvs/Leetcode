import time
import heapq
from collections import defaultdict


class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        h = []
        d = defaultdict(int)
        for num in nums:
            new_num = int("".join([str(mapping[int(d)]) for d in str(num)]))
            d[new_num] += 1
            heapq.heappush(h, (new_num, d[new_num], num))
        return [heapq.heappop(h)[2] for i in range(len(h))]


_mapping = [8,9,4,0,2,1,3,5,7,6]
_nums = [991,338,38]
# _mapping = [0,1,2,3,4,5,6,7,8,9]
# _nums = [789,456,123]

print(Solution().sortJumbled(_mapping, _nums))
