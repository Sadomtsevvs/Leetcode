from time import time


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i = j = 0
        while i < m or j < n:
            if j == n:
                res.append(nums1[i])
                i += 1
            elif i == m:
                res.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        nums1[:] = res

        # from LC comments, great
        #
        # while m > 0 and n > 0:
        #     if nums1[m-1] >= nums2[n-1]:
        #         nums1[m+n-1] = nums1[m-1]
        #         m -= 1
        #     else:
        #         nums1[m+n-1] = nums2[n-1]
        #         n -= 1
        # if n > 0:
        #     nums1[:n] = nums2[:n]


start_time = time()

_nums1 = [1, 2, 3, 0, 0, 0]
_m = 3
_nums2 = [2, 5, 6]
_n = 3

Solution().merge(_nums1, _m, _nums2, _n)
print(_nums1)

print("--- %s seconds ---" % (time() - start_time))