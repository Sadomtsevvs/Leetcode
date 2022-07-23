from time import time
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        med = nums1[0] if nums1 else nums2[0]
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        while i + j <= (len1 + len2) / 2:
            if i == len1:
                prev = med
                med = nums2[j]
                j += 1
            elif j == len2:
                prev = med
                med = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                prev = med
                med = nums1[i]
                i += 1
            else:
                prev = med
                med = nums2[j]
                j += 1
        return med if (len1 + len2) % 2 == 1 else (med + prev) / 2




start_time = time()

_nums1 = [1,2]
_nums2 = [3,4]

print(Solution().findMedianSortedArrays(_nums1, _nums2))

print("--- %s seconds ---" % (time() - start_time))
