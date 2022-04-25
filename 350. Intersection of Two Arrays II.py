from time import time
from collections import defaultdict


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict1 = defaultdict(int)
        for num in nums1:
            dict1[num] += 1
        dict2 = defaultdict(int)
        for num in nums2:
            dict2[num] += 1
        result = []
        for key, value in dict1.items():
            if key in dict2:
                result += [key] * min(value, dict2[key])
        return result


start_time = time()

_nums1 = [4,9,5]
_nums2 = [9,4,9,8,4]
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

print(Solution().intersect(_nums1, _nums2))


print("--- %s seconds ---" % (time() - start_time))