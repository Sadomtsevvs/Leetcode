from time import time
from heapq import *


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:

        children = [[] for i in range(len(s))]
        for i, j in enumerate(parent):
            if j >= 0:
                children[j].append(i)

        result = [0]

        def dfs(parent_idx):
            heap = []
            heapify(heap)
            for child_idx in children[parent_idx]:
                cur = dfs(child_idx)
                if s[parent_idx] != s[child_idx]:
                    heappush(heap, -cur)
            if len(heap) == 0:
                longest_child_path = 0
                longest_child_path2 = 0
            elif len(heap) == 1:
                longest_child_path = -heappop(heap)
                longest_child_path2 = 0
            else:
                longest_child_path = -heappop(heap)
                longest_child_path2 = -heappop(heap)
            result[0] = max(result[0], longest_child_path + longest_child_path2 + 1)
            return longest_child_path + 1

        dfs(0)
        return result[0]

        # from LC comments
        #
        # children = [[] for i in range(len(s))]
        # for i, j in enumerate(parent):
        #     if j >= 0:
        #         children[j].append(i)
        #
        # res = [0]
        #
        # def dfs(i):
        #     candi = [0, 0]
        #     for j in children[i]:
        #         cur = dfs(j)
        #         if s[i] != s[j]:
        #             candi.append(cur)
        #
        #     candi = nlargest(2, candi)
        #     res[0] = max(res[0], candi[0] + candi[1] + 1)
        #     return max(candi) + 1
        #
        # dfs(0)
        # return res[0]


start_time = time()

_parent = [-1,0,0,1,1,2]
_s = "abacbe"
# _parent = [-1,0,0,0]
# _s = "aabc"
# _parent = [-1,0,1]
# _s = "aab"
_parent = [-1,137,65,60,73,138,81,17,45,163,145,99,29,162,19,20,132,132,13,60,21,18,155,65,13,163,125,102,96,60,50,101,100,86,162,42,162,94,21,56,45,56,13,23,101,76,57,89,4,161,16,139,29,60,44,127,19,68,71,55,13,36,148,129,75,41,107,91,52,42,93,85,125,89,132,13,141,21,152,21,79,160,130,103,46,65,71,33,129,0,19,148,65,125,41,38,104,115,130,164,138,108,65,31,13,60,29,116,26,58,118,10,138,14,28,91,60,47,2,149,99,28,154,71,96,60,106,79,129,83,42,102,34,41,55,31,154,26,34,127,42,133,113,125,113,13,54,132,13,56,13,42,102,135,130,75,25,80,159,39,29,41,89,85,19]
_s = "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"
# Input: parent = [-1,0,0,1,1,2], s = "abacbe"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different characters in the tree
# is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
# It can be proven that there is no longer path that satisfies the conditions.

print(Solution().longestPath(_parent, _s))

print("--- %s seconds ---" % (time() - start_time))
