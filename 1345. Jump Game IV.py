from time import time
from typing import List
from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:

        indexes = defaultdict(list)
        for i in range(len(arr)):
            indexes[arr[i]].append(i)

        result = -1
        seen = {0}
        next_idxs = [0]

        while next_idxs:
            result += 1
            next_next_idxs = set()
            for next_ind in next_idxs:
                if next_ind == len(arr) - 1:
                    return result
                for next_next_ind in (next_ind - 1, next_ind + 1):
                    if next_next_ind in seen:
                        continue
                    if next_next_ind < 0:
                        continue
                    seen.add(next_next_ind)
                    next_next_idxs.add(next_next_ind)
                for next_next_ind in indexes[arr[next_ind]]:
                    if next_next_ind in seen:
                        continue
                    next_next_idxs.add(next_next_ind)
                    seen.add(next_next_ind)
                del indexes[arr[next_ind]]
            next_idxs = list(next_next_idxs)

        # my first dfs solution, TLE
        #
        # min_jumps = {i: len(arr) for i in range(len(arr))}
        #
        # indexes = defaultdict(list)
        # for i in range(len(arr)):
        #     indexes[arr[i]].append(i)
        #
        # def dfs(cur_ind, cur_jumps):
        #     if cur_ind < 0 or cur_ind == len(arr):
        #         return
        #     if min_jumps[cur_ind] <= cur_jumps:
        #         return
        #     min_jumps[cur_ind] = cur_jumps
        #
        #     for next_ind in (cur_ind - 1, cur_ind + 1):
        #         dfs(next_ind, cur_jumps + 1)
        #
        #     for next_ind in indexes[arr[cur_ind]]:
        #         # idxs = indexes[arr[cur_ind]]
        #         # for i in range(len(idxs) - 1, -1, -1):
        #         #     next_ind = idxs[i]
        #         if next_ind == cur_ind:
        #             continue
        #         dfs(next_ind, cur_jumps + 1)
        #
        # dfs(0, 0)
        #
        # return min_jumps[len(arr) - 1]


start_time = time()

_arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
#
# _arr = [7]
# Example 2:
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
#
# _arr = [7,6,9,6,9,6,9,7]
# Example 3:
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

_arr = [7,7,7,7,7,7,7,7,7,7,11]

print(Solution().minJumps(_arr))

print("--- %s seconds ---" % (time() - start_time))
