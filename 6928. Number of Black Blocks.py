from functools import cache
from time import time
from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:

        coordinates = set((x, y) for x, y in coordinates)

        ans = [0, 0, 0, 0, 0]
        for i in range(m - 1):
            for j in range(n - 1):
                cnt = 0
                for x, y in ((0, 0), (0, 1), (1, 0), (1, 1)):
                    if (i + x, j + y) in coordinates:
                        cnt += 1
                ans[cnt] += 1

        return ans

        # winner solution
        #
        # c = defaultdict(int)
        # for x, y in coordinates:
        #     for dx in range(-1, 1):
        #         for dy in range(-1, 1):
        #             nx, ny = x+dx, y+dy
        #             if nx < 0 or nx >= m-1 or ny < 0 or ny >= n-1: continue
        #             c[(nx, ny)] += 1
        # ret = [0] * 5
        # for v in c.values():
        #     ret[v] += 1
        # ret[0] = (m-1) * (n-1) - sum(ret[1:])
        # return ret

        # another good solution
        #
        # d = defaultdict(int)
        # ds = [(-1, 0), (0, -1), (-1, -1), (0, 0)]
        # for a, b in ls:
        #     for da, db in ds:
        #         a2, b2 = a + da, b + db
        #         if 0 <= a2 < m-1 and 0 <= b2 < n-1:
        #             d[(a2,b2)] += 1
        # # print(d.items())
        # ans = [0] * 5
        # count = 0
        # for val in d.values():
        #     ans[val] += 1
        #     count += 1
        # ans[0] += (m - 1) * (n - 1) - count
        # return ans

        # another good solution
        #
        # cnt = Counter()
        # for x, y in coordinates:
        #     for i in range(x-1, x+1):
        #         for j in range(y-1, y+1):
        #             if 0 <= i < m - 1 and 0 <= j < n - 1:
        #                 cnt[(i, j)] += 1
        # tmp = Counter(cnt.values())
        # return [(n - 1) * (m - 1) - sum(tmp.values()), tmp[1], tmp[2], tmp[3], tmp[4]]


start_time = time()

# Example 1:
# Input: m = 3, n = 3, coordinates = [[0,0]]
# Output: [3,1,0,0,0]
# Explanation: The grid looks like this:
# There is only 1 block with one black cell, and it is the block starting with cell [0,0].
# The other 3 blocks start with cells [0,1], [1,0] and [1,1]. They all have zero black cells.
# Thus, we return [3,1,0,0,0].
#
# Example 2:
# Input: m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]
# Output: [0,2,2,0,0]
# Explanation: The grid looks like this:
# There are 2 blocks with two black cells (the ones starting with cell coordinates [0,0] and [0,1]).
# The other 2 blocks have starting cell coordinates of [1,0] and [1,1]. They both have 1 black cell.
# Therefore, we return [0,2,2,0,0].

# Input:
# 22
# 73
# [[11,14],[16,11],[20,5],[5,33],[14,7],[16,60],[0,15],[15,72],[6,60],[9,16],[14,51],[1,52],[18,24],[17,30],[3,4],[19,13],[9,10],[11,40],[15,7],[13,62],[8,41],[12,71],[4,72],[18,7],[1,0],[4,35],[16,33],[7,30],[13,52],[5,1],[15,21],[3,59],[2,41],[4,28]]
# Output:
# [1464,46,2,0,0]
# Expected:
# [1387,122,3,0,0]

print(Solution().minimumBeautifulSubstrings(_s))

print("--- %s seconds ---" % (time() - start_time))
