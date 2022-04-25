from time import time


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # return list(set(nums1).intersection(set(nums2)))

        result = []
        one, two = 0, 0
        while one < len(nums1) and two < len(nums2):
            if nums1[one] == nums2[two]:
                result.append(nums1[one])
                while one < len(nums1) and nums1[one] == result[-1]:
                    one += 1
                while two < len(nums2) and nums2[two] == result[-1]:
                    two += 1
            elif nums1[one] < nums2[two]:
                one += 1
            else:
                two += 1
        return result

# This is a Facebook interview question.
# They ask for the intersection, which has a trivial solution using a hash or a set.
#
# Then they ask you to solve it under these constraints:
# O(n) time and O(1) space(the resulting array of intersections is not taken into consideration).
# You are told the lists are sorted.
#
# Cases to take into consideration include:
# duplicates, negative values, single value lists, 0's, and empty list arguments.
# Other considerations might include sparse arrays.
#
# function
# intersections(l1, l2)
# {
#     l1.sort((a, b) = > a - b) // assume
# sorted
# l2.sort((a, b) = > a - b) // assume
# sorted
# const
# intersections = []
# let
# l = 0, r = 0;
# while ((l2[l] & & l1[r]) !== undefined) {
# const left = l1[r], right = l2[l];
# if (right == = left) {
# intersections.push(right)
# while (left === l1[r]) r++;
# while (right === l2[l]) l++;
# continue;
# }
# if (right > left)
#     while (left === l1[r]) r++;
#     else while (right == = l2[l]) l++;
#
# }
# return intersections;
# }


start_time = time()

_nums1 = [4,9,5]
_nums2 = [9,4,9,8,4]
# example for Facebook
_nums1 = [4,5, 9]
_nums2 = [4,4,8,9,9]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

print(Solution().intersection(_nums1, _nums2))

print("--- %s seconds ---" % (time() - start_time))
