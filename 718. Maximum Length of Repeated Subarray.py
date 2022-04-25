from time import time


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        result = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    result[i][j] = 1 + result[i-1][j-1]
        return max(max(s) for s in result)


start_time = time()

_nums1 = [1,2,3,2,1,7,8,9,8]
_nums2 = [3,2,1,4,7,8,9,8]
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].

print(Solution().findLength(_nums1, _nums2))

print("--- %s seconds ---" % (time() - start_time))
