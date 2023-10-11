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

        # official solution
        #
        # na, nb = len(A), len(B)
        # n = na + nb
        #
        # def solve(k, a_start, a_end, b_start, b_end):
        #     # If the segment of on array is empty, it means we have passed all
        #     # its element, just return the corresponding element in the other array.
        #     if a_start > a_end:
        #         return B[k - a_start]
        #     if b_start > b_end:
        #         return A[k - b_start]
        #
        #     # Get the middle indexes and middle values of A and B.
        #     a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
        #     a_value, b_value = A[a_index], B[b_index]
        #
        #     # If k is in the right half of A + B, remove the larger right half.
        #     if a_index + b_index < k:
        #         if a_value > b_value:
        #             return solve(k, a_start, a_end, b_index + 1, b_end)
        #         else:
        #             return solve(k, a_index + 1, a_end, b_start, b_end)
        #     # Otherwise, remove the smaller left half.
        #     else:
        #         if a_value > b_value:
        #             return solve(k, a_start, a_index - 1, b_start, b_end)
        #         else:
        #             return solve(k, a_start, a_end, b_start, b_index - 1)
        #
        # if n % 2:
        #     return solve(n // 2, 0, na - 1, 0, nb - 1)
        # else:
        #     return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) + solve(n // 2, 0, na - 1, 0, nb - 1)) / 2


start_time = time()

_nums1 = [1,2]
_nums2 = [3,4]

print(Solution().findMedianSortedArrays(_nums1, _nums2))

print("--- %s seconds ---" % (time() - start_time))
