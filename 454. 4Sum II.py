from collections import defaultdict
from time import time
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n1n2 = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                n1n2[n1+n2] += 1
        n3n4 = defaultdict(int)
        for n3 in nums3:
            for n4 in nums4:
                n3n4[n3+n4] += 1
        ans = 0
        for s in n1n2:
            ans += n1n2[s] * n3n4[-s]
        return ans

        # solution from Pochmann
        #
        # AB = collections.Counter(a + b for a in A for b in B)
        # return sum(AB[-c - d] for c in C for d in D)

        # from LC, cool, less space than me
        #
        # res = 0
        # twoSums = collections.defaultdict(int)
        # for a in A:
        #     for b in B:
        #         twoSums[a + b] += 1
        # for c in C:
        #     for d in D:
        #         res += twoSums[-(c + d)]
        # return res


start_time = time()

_nums1 = [1,2]
_nums2 = [-2,-1]
_nums3 = [-1,2]
_nums4 = [0,2]
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

print(Solution().fourSumCount(_nums1, _nums2, _nums3, _nums4))

print("--- %s seconds ---" % (time() - start_time))
