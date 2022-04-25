from time import time


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max1 = max2 = max3 = -float("inf")
        for num in nums:
            if num > max1:
                if max2 != -float("inf"):
                    max3 = max2
                if max1 != -float("inf"):
                    max2 = max1
                max1 = num
            elif num > max2 and num < max1:
                if max2 != -float("inf"):
                    max3 = max2
                max2 = num
            elif num > max3 and num < max2:
                max3 = num
        return max3 if max3 != -float("inf") else max(max1, max2)


start_time = time()

_nums = [-8,2,2,1, -9]
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

print(Solution().thirdMax(_nums))

print("--- %s seconds ---" % (time() - start_time))
