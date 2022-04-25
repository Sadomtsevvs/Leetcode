from time import time


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {nums2[-1]: -1}
        prev = nums2[-1]
        for i in range(len(nums2)-2, -1, -1):
            while nums2[i] > prev != -1:
                prev = d[prev]
            d[nums2[i]] = prev
            prev = nums2[i]
        return [d[num] for num in nums1]

        # from LC comments
        #
        # dic, stack = {}, []
        #
        # for num in nums2[::-1]:
        #     while stack and num > stack[-1]:
        #         stack.pop()
        #     if stack:
        #         dic[num] = stack[-1]
        #     stack.append(num)
        #
        # return [dic.get(num, -1) for num in nums1]


start_time = time()

_nums1 = [4,1,2]
_nums2 = [1,3,4,2]
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

print(Solution().nextGreaterElement(_nums1, _nums2))

print("--- %s seconds ---" % (time() - start_time))
