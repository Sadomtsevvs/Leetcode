from time import time


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers1 = list(map(int, version1.split('.')))
        vers2 = list(map(int, version2.split('.')))
        if len(vers1) > len(vers2):
            vers2 += [0] * (len(vers1) - len(vers2))
        elif len(vers1) < len(vers2):
            vers1 += [0] * (len(vers2) - len(vers1))
        for i in range(len(vers1)):
            if vers1[i] > vers2[i]:
                return 1
            elif vers1[i] < vers2[i]:
                return -1
        return 0

        # official solution
        #
        # nums1 = version1.split('.')
        # nums2 = version2.split('.')
        # n1, n2 = len(nums1), len(nums2)
        #
        # # compare versions
        # for i in range(max(n1, n2)):
        #     i1 = int(nums1[i]) if i < n1 else 0
        #     i2 = int(nums2[i]) if i < n2 else 0
        #     if i1 != i2:
        #         return 1 if i1 > i2 else -1
        #
        # # the versions are equal
        # return 0


start_time = time()

_version1 = "1.01"
_version2 = "1.001"
# Example 1:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
#
# Example 2:
# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 does not specify revision 2, which means it is treated as "0".
#
# Example 3:
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

print(Solution().compareVersion(_version1, _version2))

print("--- %s seconds ---" % (time() - start_time))
