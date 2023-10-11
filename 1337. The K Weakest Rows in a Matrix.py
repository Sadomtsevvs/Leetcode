from time import time
import heapq


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:

        heap = []
        heapq.heapify(heap)
        for i, row in enumerate(mat):
            heapq.heappush(heap, (row.count(1), i))
        return [heapq.heappop(heap)[1] for _ in range(k)]

        # my first solution
        #
        # heap = []
        # heapq.heapify(heap)
        # for row in range(len(mat)):
        #     heapq.heappush(heap, mat[row].count(1) + row / 100)
        # result = []
        # for _ in range(k):
        #     el = heapq.heappop(heap)
        #     result.append(round((el - int(el))*100))
        # return result

        # Solution from LC comments
        #
        # m, n = len(mat), len(mat[0])
        # result = {}
        # for j in range(n):
        #     for i in range(m):
        #         if mat[i][j] or i in result:
        #             continue
        #         result[i] = True
        #         k -= 1
        #         if not k:
        #             return result.keys()
        # for i in range(m):
        #     if i not in result:
        #         result[i] = True
        #         k -= 1
        #         if not k:
        #             return result.keys()

        # nice solution from LC comments
        #
        # for index, arr in enumerate(mat):
        #     arr.append(index)
        # mat.sort()
        # return [arr[-1] for arr in mat[:k]]


start_time = time()

_mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
_k = 2
# _mat = [[1,1,0,0,0],
#         [1,1,1,1,0],
#         [1,0,0,0,0],
#         [1,1,0,0,0],
#         [1,1,1,1,1]]
# _k = 3
# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]
# Explanation:
# The number of soldiers in each row is:
# - Row 0: 2
# - Row 1: 4
# - Row 2: 1
# - Row 3: 2
# - Row 4: 5
# The rows ordered from weakest to strongest are [2,0,3,1,4].

print(Solution().kWeakestRows(_mat, _k))

print("--- %s seconds ---" % (time() - start_time))
